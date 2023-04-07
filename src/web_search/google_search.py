import asyncio
from googleapiclient.discovery import build

from web_search.request_throttler import RequestThrottler

google_search_throttler = RequestThrottler()

class Google:
    def __init__(self):
        self.api_key = "AIzaSyB3RhZrp0ndu2FY5BsiM5EQr-9u9CIi1xU"
        self.cx = "7226b80805cf44a68"
        self.service = build("customsearch", "v1", developerKey=self.api_key)

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
        # TODO: Make the search async
        res = self.service.cse().list(q=q, cx=self.cx, num=num, start=start).execute()
        if "items" in res:
            return [item["link"] for item in res["items"]]
        else:
            return []
