import asyncio.exceptions
import sys
from typing import Union
import aiohttp
from data.search_history import SearchHistory
from web_search.request_throttler import RequestThrottler

OPENAI_MAX_PROMPT_LEN = 1000


openai_throttler = RequestThrottler("OpenAI")

class OpenAI:
    def __init__(self):
        self.key = "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"
        self.organization = "org-nVcfRvKHlZzuZmUk3kTRiXMP"
        self.endpoint = "https://api.openai.com/v1/chat/completions"

    async def __request(self, messages):
        data = {
                    "model": "gpt-3.5-turbo",
                    "messages": messages,
                    "temperature": 0.1,
                    "max_tokens": 2000,
                    "frequency_penalty": 0,
                    "presence_penalty": 1.1,
                }
        print(messages)
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as session:
            headers = {"Authorization": f"Bearer {self.key}"}
            async with session.post(self.endpoint, headers=headers, json=data) as resp:
                return await resp.json()
    
    async def __chat(self, system_message: str, user_prompt_message: str) -> str:
        """Send a prompt message to the assistant. Return their response"""

        # create the message history
        chat_messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_prompt_message}
        ]

        # repeatedly prompt chatgpt. if it throws an error, retry up to 3 times
        for i in range(3):
            try:
                await openai_throttler.throttle_request("Prompt length: "+str(len(user_prompt_message)))
                response_obj = await self.__request(chat_messages)
                text_response: str = response_obj["choices"][0]['message']['content'].strip()
                return text_response
            except KeyError:
                print("received error message: " + str(response_obj), file=sys.stderr)
                print("retrying " + str(3-i) + " more times")
                continue
            except asyncio.TimeoutError or asyncio.exceptions.TimeoutError as e:
                raise e
        
        return ""

    async def get_search_keywords(self, history: SearchHistory) -> list[str]:
        # get the keyword and the context from the search history
        keyword_history = history.get_keyword_history()
        context = " > ".join(keyword_history[:-1])  # Example: 'animals > dogs'
        keyword = keyword_history[-1]  # Example: 'beagle'

        # create a prompt for chat-gpt to get useful search terms
        system_message = "You are a research assistant that can come up with child topics related to the keywords and topics provided in a bulleted list in descending order of relevance to the main topic. Do not number the list. Each item in the list should also serve as a useful search query for Google or Bing to find out more about the topic. The total number of child topics cannot exceed 5 and there can only be a total of 6 words per child topic."
        if context:
            user_prompt = f"What are some relevant child topics for the following query: '{keyword}', given that its parent topic is '{context}'?"
        else:
            user_prompt = f"What are some relevant child topics for the following query: '{keyword}'?"
        
        # send the chat message & format the response as a list of keyword topics
        text_response = await self.__chat(system_message, user_prompt)
        response = self.__format(text_response, format='return_list')
        return response

    async def summarize(self, keyword: str, web_content_summary: str) -> str:
        """Return a description of a keyword given a summary of scraped web content"""

        # prevent large prompts
        if len(web_content_summary) > OPENAI_MAX_PROMPT_LEN:
            web_content_summary = web_content_summary[:OPENAI_MAX_PROMPT_LEN]
        
        # create a prompt for chat-gpt to summarize a topic given web content
        system_message = "You are an assistant that can provide accurate and concise descriptions of topics. The user will provide a computer-generated summary of content scraped from the web that may or may not be useful for your task."
        user_prompt = f"Write a 3-sentence description of: '{keyword}'. Here is some info about '{keyword}' I scraped from the web: {web_content_summary}"

        # send the chat message & format the response as a list of keyword topics
        text_response = await self.__chat(system_message, user_prompt)
        response = self.__format(text_response, format='return_str')
        return response

    def __format(self, text_response: str, format:Union['return_list','return_str','auto']='auto'):
        # extract the text from ChatGPT's response, and split it into lines
        response_lines: list[str] = text_response.split("\n")

        if format == 'return_str':
            return text_response

        # If there's only one line, return it as a string
        if len(response_lines) == 1 and format == 'auto':
            return response_lines[0]

        # If there's many lines, we assume ChatGPT was giving us a list.
        # Return the list, but remove the bullet points

        # first, identify the separator token
        first_elem = response_lines[0]
        sep: str = None
        if first_elem.startswith('-') or first_elem.startswith(' -'):
            sep = '-'
        elif '.q ' in first_elem:
            sep = '.q '

        if sep is not None:
            return [elem.split(sep)[1] for elem in response_lines]
        else:
            return response_lines
