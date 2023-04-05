import asyncio
from searches.openai_search import OpenAI
import searches.google_search as google
from searches.bing_search import Bing
import flask


class SearchController:
    def __init__(self):
        # query = "iasubyaseiruntgiuaydhfbi auhergi uhaedfkbn wiertuh skdjhn wseirtuyh df "
        # self.bingSearcher = Bing()
        # response = self.bingSearcher.search(query)
        # print(response)
        #
        # response = asyncio.run(google.search(query, 10, 10, 10))
        # print(response)
        openai = OpenAI()
        response = openai.chat("what are some categories for the following phrase: Pokemon")
        print(response)

if __name__ == "__main__":
    main = SearchController()