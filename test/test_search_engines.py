import asyncio
from web_search.bing_search import Bing
from web_search.google_search import Google

def test_google_search():
    google = Google()
    results = asyncio.run(google.search("dog", count=5))
    assert len(results) > 0 and results[0].startswith("http")

def test_nonsense_google_search():
    google = Google()
    results = asyncio.run(google.search("23fh42389h97", count=5))
    assert len(results) == 0

def test_bing_search():
    bing = Bing()
    results = asyncio.run(bing.search("dog", count=5))
    assert len(results) > 0 and results[0].startswith("http")

def test_nonsense_bing_search():
    bing = Bing()
    results = asyncio.run(bing.search("23fh42389h97", count=5))
    assert len(results) == 0

