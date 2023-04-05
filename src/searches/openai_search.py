import json
import aiohttp
import asyncio


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

    async def categorize(self, prompt):
        response = await self._request("completions", {
            "model": "text-davinci-003",
            "prompt": f"what are some categories for the following phrase: {prompt}",
            "temperature": 0.1,
            "max_tokens": 1000,
            "top_p": 1,
            "best_of": 1,
            "frequency_penalty": 0,
            "presence_penalty": 1.1,
        })

        return self.__format__(response)

    async def summarize(self, prompt):
        response = await self._request("completions", {
            "model": "text-davinci-003",
            "prompt": "summarize this: " + prompt,
            "temperature": 0.1,
            "max_tokens": 1000,
            "top_p": 1,
            "best_of": 2,
            "frequency_penalty": 0,
            "presence_penalty": 1.1,
        })

        return self.__format__(response)

    def __format__(self, response):
        response = response["choices"][0]["text"].strip().split("\n")

        if len(response) == 1:
            return response[0]

        return [elem.split('.q ')[1] for elem in response]
