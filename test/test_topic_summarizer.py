import asyncio
from data.web_content import WebContent
from openai_api import OpenAI
from topic_summarizer import TopicSummarizer

# create dummy websites for the test
mock_pages: dict[str, WebContent] = {
    "https://www.pokemon.com/us": WebContent(
        title="Pokemon Website",
        content="This is the content of pokemon.com",
        url="https://www.pokemon.com/us"
    ), 
    "https://en.wikipedia.org/wiki/Pok%C3%A9mon": WebContent(
        title="Pokemon Wiki",
        content="Pokemon wiki content",
        url="https://en.wikipedia.org/wiki/Pok%C3%A9mon"
    ),
    "https://en.wikipedia.org/wiki/Nintendo": WebContent(
        title="Nintendo Wiki",
        content="Nintendo wiki content",
        url="https://en.wikipedia.org/wiki/Nintendo"
    )
}

# create dummy summaries for the test
mock_summaries: dict[str, str] = {
    "This is the content of pokemon.com":
        "This page should not be summarized.", 

    "Pokemon wiki content":
        "Pokemon Wiki Summary.",

    "Nintendo wiki content": 
        "Nintendo Wiki Summary."
}

# create dummy download & summarize functions
async def mock_download_page(url: str) -> WebContent:
    assert url in mock_pages.keys()
    return mock_pages[url]

def mock_summarize(content: str,
                    keywords: list[str]=[],
                    max_summary_length: str = 1000,
                    min_sent_len = 30,
                    max_sent_len = 250,
                    top_n_words = 50
                    ):
    assert keywords[0] == 'pokemon'
    assert content in mock_summaries.keys()
    return mock_summaries[content]


class MockOpenAI(OpenAI):
    """Use a mock instance of OpenAI so we don't have to make actual API requests."""

    async def get_search_keywords(self, history) -> list[str]:
        raise "Do not call this"

    async def summarize(self, keyword: str, web_content_summary: str) -> str:
        assert keyword == "pokemon"
        assert web_content_summary == "Pokemon Wiki Summary.Nintendo Wiki Summary."
        return f"pokemon summary"


def test_topic_summarizer():

    # create the mock summarizer
    topic_summarizer = TopicSummarizer()
    
    # inject mock dependencies
    topic_summarizer.open_ai = MockOpenAI()
    topic_summarizer.download_page_fn = mock_download_page
    topic_summarizer.summarize_page_content_fn = mock_summarize

    # get topic results
    topic_results = asyncio.run(topic_summarizer.summarize_topic(list(mock_pages.keys()), "pokemon"))

    # validate name & description
    assert topic_results.get_topic_description() == 'pokemon summary'
    assert topic_results.get_topic_name() == 'pokemon'

    # validate urls
    urls = topic_results.get_urls()
    assert len(urls) == 3

    assert urls[0].get_link() == "https://en.wikipedia.org/wiki/Pok%C3%A9mon"
    assert urls[0].get_category().get_category_name() == "Wiki"
    assert urls[0].name == "Pokemon Wiki: en.wikipedia.org"

    assert urls[1].get_link() == "https://en.wikipedia.org/wiki/Nintendo"
    assert urls[1].get_category().get_category_name() == "Wiki"
    assert urls[1].name == "Nintendo Wiki: en.wikipedia.org"

    assert urls[2].get_link() == "https://www.pokemon.com/us"
    assert urls[2].get_category().get_category_name() == "Other"
    assert urls[2].name == "Pokemon Website: pokemon.com"
