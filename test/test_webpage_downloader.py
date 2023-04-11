import asyncio
import pytest

from web_search.webpage_downloader import download_page


def test_fake_website():
    page = asyncio.run(download_page("http://fakewebsite3489248.io"))
    assert page.content == "" and page.url == "http://fakewebsite3489248.io" and page.page_title == ""

def test_blank_website():
    page = asyncio.run(download_page("https://blank.page/"))
    assert page.content == "Blank Page" and page.page_title == "dsafsa" and page.url == "https://blank.page/"

def test_regular_website():
    page = asyncio.run(download_page("https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP"))
    assert "Natural language processing (NLP) is the ability of a computer program to understand human language" in page.content and \
        "</span>" not in page.content

