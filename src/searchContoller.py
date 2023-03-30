import asyncio
from searches.openai_search import OpenAI
import searches.google_search as google
from searches.bing_search import Bing
import flask


class SearchController:
    def __init__(self):
        self.bingSearcher = Bing()
        response = self.bingSearcher.search("orthogonal vectors")
        print(response)

        response = asyncio.run(google.search('orthogonal vectors', 10, 10, 10))
        print(response)


if __name__ == "__main__":
    main = SearchController()