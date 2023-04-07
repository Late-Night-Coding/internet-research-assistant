from web_search.bing_search import Bing
from web_search.google_search import Google


class SearchAggregator:
    def __init__(self):
        self.bing_searcher = Bing()
        self.google_searcher = Google()

    async def search(self, query):
        bingResults = await(self.bing_searcher.search(query))
        googleResults = await(self.google_searcher.search(query))

        return [*bingResults, *googleResults]

        
