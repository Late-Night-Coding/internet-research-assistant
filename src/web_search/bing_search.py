import aiohttp
from web_search.request_throttler import RequestThrottler


bing_search_throttler = RequestThrottler("Bing")

class Bing:
    def __init__(self):
        self.key1 = "0000-0000"
        self.key2 = "0000-0000"
        self.search_url = "https://api.bing.microsoft.com/v7.0/search"
        self.headers = {"Ocp-Apim-Subscription-Key": self.key1}

    async def search(self, search_term, count=10) -> list[str]:
        params = {"q": search_term, "textDecorations": "true", "textFormat": "HTML", "count": count, "responseFilter": "Webpages"}
        await bing_search_throttler.throttle_request()

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.search_url, params=params) as response:
                response.raise_for_status()
                search_results = await response.json()

        if "webPages" in search_results:
            search_results = [page["url"] for page in search_results["webPages"]["value"]]
        else:
            search_results = []

        return search_results
