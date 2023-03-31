import bing_search
import google_search
import openai_search

class Search:

    def __init__(self):
        self.bing_searcher = bing_search.Bing()
        self.openai_searcher = openai_search.OpenAI()

        self.bing_search_result = list()
        self.google_search_result = list()
        self.openai_query_result = None

    def search(self, query, num, stop, pause):
        self.bing_searcher.search(query)
