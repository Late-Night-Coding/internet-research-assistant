import asyncio
from data.research_results import ResearchResults
from data.search_history import SearchHistory
from data.topic_results import TopicResults
from openai_api import OpenAI
from search_controller import SearchController
from search_processor import SearchProcessor

# create dummy data
animal_results = ResearchResults()
animal_results.add_topic(TopicResults('dog facts', '', []))
animal_results.add_topic(TopicResults('cat facts', '', []))

dog_results = ResearchResults()
dog_results.add_topic(TopicResults('beagle', '', []))
dog_results.add_topic(TopicResults('pitbull', '', []))

research_results: dict[tuple[str], ResearchResults] = {
    ('dog facts', 'cat facts'): animal_results,
    ('beagle', 'pitbull'): dog_results,
}

# create dummy services
class MockSearchProcessor(SearchProcessor):
    async def search(self, keywords: list[str]) -> ResearchResults:
        return research_results[tuple(keywords)]
    
class MockOpenAI(OpenAI):
    """Use a mock instance of OpenAI so we don't have to make actual API requests."""

    async def get_search_keywords(self, history: SearchHistory) -> list[str]:

        # First search
        if len(history.keyword_history) == 1:
            assert history.keyword_history == ['animal fact']
            return ['dog facts', 'cat facts']

        # Second search
        elif len(history.keyword_history) == 2:
            assert history.keyword_history == ['animal fact', 'dog breed']
            return ['beagle', 'pitbull']

        else:
            raise "Expected either 1 or 2 entries in the search history"

    async def summarize(self, keyword: str, web_content_summary: str) -> str:
        raise "Do not call this"

    
def test_search_controller():

    # Create the search controller
    search_controller = SearchController()

    # Inject mock dependencies for testing
    search_controller.search_processor = MockSearchProcessor()
    search_controller.open_ai = MockOpenAI()

    # Test first search
    first_search_results, first_search_id = asyncio.run(search_controller.search('animal facts'))
    assert first_search_id is not None
    assert first_search_results == animal_results

    # Test second search
    second_search_results, second_search_id = asyncio.run(search_controller.search('dog breeds', search_id=first_search_id)) 
    assert second_search_id == first_search_id
    assert second_search_results == dog_results


