import searches.bing_search as bing_search
import searches.google_search as google_search
import searches.openai_search as openai_search

class Search:

    def __init__(self):
        #print("Search object has been created")
        self.bing_searcher = bing_search.Bing()
        self.google_searcher = google_search.Google()
        self.openai_searcher = openai_search.OpenAI()

        self.bing_search_result = list()
        self.google_search_result = list()
        self.openai_query_result = None

    async def search(self, query):
        self.bingResults = await(self.bing_searcher.search(query))
        self.googleResults = await(self.google_searcher.search(query))

        return [self.bingResults, self.googleResults]

        
