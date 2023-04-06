import aiohttp

class Bing:
    def __init__(self):
        self.key1 = "a545213acdb4407c9f3fffc6097f9b67"
        self.key2 = "ebf8de5d4f9240ea9911a24d2c25d9d9"
        self.search_url = "https://api.bing.microsoft.com/v7.0/search"
        self.headers = {"Ocp-Apim-Subscription-Key": self.key1}

    async def search(self, search_term, count=10):
        params = {"q": search_term, "textDecorations": "true", "textFormat": "HTML", "count": count, "responseFilter": "Webpages"}

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.search_url, params=params) as response:
                response.raise_for_status()
                search_results = await response.json()

        if "webPages" in search_results:
            search_results = [page["url"] for page in search_results["webPages"]["value"]]
        else:
            search_results = []

        return search_results
