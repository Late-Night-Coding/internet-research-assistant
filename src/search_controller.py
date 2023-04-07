from openai_api import OpenAI
from data.search_history import SearchHistory
from nlp.input_parser import InputParser
from search_processor import SearchProcessor
from random import randint


def generate_new_id() -> str:
    return str(randint(1, 10000000000))


class SearchController:
    def __init__(self):
        self.search_processor = SearchProcessor()
        self.input_parser = InputParser()
        self.open_ai = OpenAI()
        self.history_map: dict[str, SearchHistory] = {}

    async def search(self, query: str, search_id: str = None):
        results = None

        # extract keywords from query
        query_keyword = " ".join(self.input_parser.parse(query)[0])

        # if id==None -> a whole new search
        if search_id is None:
            search_id = generate_new_id()
            search_history = SearchHistory(query_keyword, search_id)
            self.history_map[search_id] = search_history

        # otherwise, obtain the search object
        else:
            search_history = self.history_map[search_id]
            search_history.append_keyword(query_keyword)

        # get the list of keywords in the context of the search history
        search_keywords = await self.open_ai.get_search_keywords(search_history)

        # limit the number of keywords
        if len(search_keywords) > 5:
            search_keywords = search_keywords[:5]

        results = await self.search_processor.search(search_keywords)

        return results

