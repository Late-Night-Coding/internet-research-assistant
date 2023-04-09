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
        self.endpoint = "https://api.openai.com/v1/"

    async def _request(self, endpoint, data):
        async with aiohttp.ClientSession() as session:
            headers = {"Authorization": f"Bearer {self.key}"}
            async with session.post(self.endpoint + endpoint, headers=headers, json=data) as resp:
                return await resp.json()

    async def get_search_keywords(self, history: SearchHistory) -> list[str]:
        # get the keyword and the context from the search history
        keyword_history = history.get_keyword_history()
        context = " > ".join(keyword_history[:-1])  # Example: 'animals > dogs'
        keyword = keyword_history[-1]  # Example: 'beagle'

        # create a prompt for chat-gpt to get useful search terms
        if context:
            prompt = f"What are some relevant search terms for the following query: '{keyword}', given that its parent topic is '{context}'? Format your response as a bulleted list.\nRESPONSE:\n"
        else:
            prompt = f"What are some relevant search terms for the following query: '{keyword}'? Format your response as a bulleted list.\nRESPONSE:\n"

        await openai_throttler.throttle_request("Prompt length: "+str(len(prompt)))
        response_obj = await self._request("completions", {
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 0.1,
            "max_tokens": 1000,
            "top_p": 1,
            "best_of": 1,
            "frequency_penalty": 0,
            "presence_penalty": 1.1,
        })

        return self.__format(response_obj, format='return_list')

    async def summarize(self, keyword: str, web_content_summary: str) -> str:

        # create a prompt for chat-gpt to summarize a topic given web content
        if len(web_content_summary) > OPENAI_MAX_PROMPT_LEN:
            web_content_summary = web_content_summary[:OPENAI_MAX_PROMPT_LEN]

        prompt = f"Write a 3-sentence description of: '{keyword}'. Here is some info about '{keyword}' I scraped from the web: {web_content_summary}\nRESPONSE:\n"

        await openai_throttler.throttle_request("Prompt length: "+str(len(prompt)))
        response_obj = await self._request("completions", {
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 0.1,
            "max_tokens": 1000,
            "top_p": 1,
            "best_of": 2,
            "frequency_penalty": 0,
            "presence_penalty": 1.1,
        })

        return self.__format(response_obj, format='return_str')

    def __format(self, response_obj, format:Union['return_list','return_str','auto']='auto'):
        # extract the text from ChatGPT's response, and split it into lines
        text_response: str = response_obj["choices"][0]["text"].strip()
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
