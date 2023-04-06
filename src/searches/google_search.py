import asyncio
from googleapiclient.discovery import build


class Google:
    def __init__(self):
        self.api_key = "AIzaSyB3RhZrp0ndu2FY5BsiM5EQr-9u9CIi1xU"
        self.cx = "7226b80805cf44a68"
        self.service = build("customsearch", "v1", developerKey=self.api_key)

    async def search(self, search_term, count=10):
        results = []
        if count > 100:
            raise ValueError("Number of results can't be greater than 100 due to api restrictions")
        elif count > 10:
            results.extend(self.__search(search_term))
            start = 11
            count -= 10
            remainder = count % 10
            for _ in range(int(count / 10)):
                results.extend(self.__search(search_term, 10, start))
                start += 10
            if remainder > 0:
                results.extend(self.__search(search_term, remainder, start))
        else:
            results.extend(self.__search(search_term))

        return results

    def __search(self, q, num=10, start=0) -> list:
        res = self.service.cse().list(q=q, cx=self.cx, num=num, start=start).execute()
        return [item["link"] for item in res["items"]]
