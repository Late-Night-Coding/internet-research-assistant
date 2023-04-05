import asyncio
from searches.google_search import search as google_search

def test_google_search():
    results = asyncio.run(google_search("dog", num=5))
    assert len(results) > 0 and results[0].startswith("http")

def test_nonsense_google_search():
    results = asyncio.run(google_search("23fh42389h97"))
    assert len(results) == 0

# TODO: Make bing & chatgpt async
def test_bing_search():
    raise "not implemented"
