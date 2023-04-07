import aiohttp

from web_search.request_throttler import RequestThrottler



class Google:
    def __init__(self):
        self.api_key = "AIzaSyB3RhZrp0ndu2FY5BsiM5EQr-9u9CIi1xU"
        self.cx = "7226b80805cf44a68"
        self.search_url = "https://www.googleapis.com/customsearch/v1"
        self.google_search_throttler = RequestThrottler()

    async def search(self, search_term: str, count=10) -> list[str]:
        results = []
        if count > 100:
            raise ValueError("Number of results can't be greater than 100 due to api restrictions")
        elif count > 10:
            results.extend(await self.__search(search_term))
            start = 11
            count -= 10
            remainder = count % 10
            for _ in range(int(count / 10)):
                results.extend(await self.__search(search_term, 10, start))
                start += 10
            if remainder > 0:
                results.extend(await self.__search(search_term, remainder, start))
        else:
            results.extend(await self.__search(search_term))

        return results

    async def __search(self, q, num=10, start=0) -> list:
        await self.google_search_throttler.throttle_request()

        # make the async search
        async with aiohttp.ClientSession() as session:
            params = {
                "key": self.api_key,
                "cx": self.cx,
                "q": q,
                "num": num,
                "start": start
            }
            async with session.get(self.search_url, params=params) as response:
                response.raise_for_status()
                res = await response.json()

        if "items" in res:
            return [item["link"] for item in res["items"]]
        else:
            return []
