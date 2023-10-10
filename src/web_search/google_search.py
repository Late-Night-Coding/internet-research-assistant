import aiohttp

from web_search.request_throttler import RequestThrottler

google_search_throttler = RequestThrottler("Google")

class Google:
    def __init__(self):
        self.api_key = "0000-0000"
        self.cx = "0000-0000"
        self.search_url = "0000-0000"

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
        await google_search_throttler.throttle_request()

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
