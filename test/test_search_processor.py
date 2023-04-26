
import asyncio
from data.topic_results import TopicResults
from search_processor import SearchProcessor
from topic_summarizer import TopicSummarizer
from web_search.search_aggregator import SearchAggregator

# create dummy data
mock_search_links: dict[str, list[str]] = {
    'pikachu': [
        'pikachu link 1',
        'pikachu link 2'
    ],

    'charzard': [
        'charzard link 1',
        'charzard link 2'
    ]
}

mock_topic_results = {
    'pikachu': TopicResults('pikachu', '', []),
    'charzard': TopicResults('charzard', '', [])
}

# create dummy services
class MockSearchAggregator(SearchAggregator):
    async def search(self, query):
        return mock_search_links[query]
    
class MockTopicSummarizer(TopicSummarizer):
    async def summarize_topic(self, links: list[str], keyword: str, summary_len: int) -> TopicResults:
        assert links == mock_search_links[keyword]
        assert summary_len == 2
        return mock_topic_results[keyword]
    
def test_search_processor():

    # Create the search processor
    search_processor = SearchProcessor()

    # Inject mock dependencies for testing
    search_processor.search_aggregator = MockSearchAggregator()
    search_processor.topic_summarizer = MockTopicSummarizer()

    # Test search
    research_results = asyncio.run(search_processor.search(['pikachu', 'charzard'], 2))

    # Validate results
    topics = research_results.get_topics()
    assert topics == [
        mock_topic_results['pikachu'],
        mock_topic_results['charzard']
    ]


