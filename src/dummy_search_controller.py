# create dummy services
import asyncio
from data.research_results import ResearchResults
from data.search_history import SearchHistory
from data.topic_results import TopicResults
from data.url import URL
from data.url_category import URLCategory
from openai_api import OpenAI
from search_controller import SearchController
from search_processor import SearchProcessor

from data.url_category import wiki_cat, youtube_cat, social_media_cat, other_cat

class DummySearchProcessor(SearchProcessor):
    async def search(self, keywords: list[str], summary_len: int) -> ResearchResults:
        await asyncio.sleep(1)
        research_results = ResearchResults()
        for keyword in keywords:
            topic_result = TopicResults(
                topic_name = keyword,
                topic_description = "This is a dummy paragraph. To see the internet research assistant in action, replace the dummy search controller with a real one.",
                url_list=[
                    URL('https://wikipedia.org/', wiki_cat, 'Wiki Link'),
                    URL('https://youtube.com/', youtube_cat, 'Youtube Link'),
                    URL('https://twitter.com/', social_media_cat, 'Twitter Link'),
                    URL("https://google.com/", other_cat, "Other Link")
                ]
            )
            research_results.add_topic(topic_result)
        return research_results

    
class DummyOpenAI(OpenAI):
    """Use a mock instance of OpenAI so we don't have to make actual API requests."""

    async def get_search_keywords(self, history: SearchHistory) -> list[str]:
        return [
            str(history) + " " + str(i)
            for i in range(3)
        ]

    async def summarize(self, keyword: str, web_content_summary: str, summay_len: int) -> str:
        raise "Do not call this"

    
def get_dummy_search_controller():
    # Create the search controller
    search_controller = SearchController()

    # Inject mock dependencies for testing
    search_controller.search_processor = DummySearchProcessor()
    search_controller.open_ai = DummyOpenAI()

    return search_controller
