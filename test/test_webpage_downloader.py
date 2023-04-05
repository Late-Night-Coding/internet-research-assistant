import asyncio
import pytest

from searches.webpage_downloader import download_page

def test_fake_website():
    page_content = asyncio.run(download_page("http://fakewebsite3489248.io"))
    assert page_content == ""

def test_blank_website():
    page_content = asyncio.run(download_page("https://blank.page/"))
    assert page_content == "Blank Page"

def test_regular_website():
    page_content = asyncio.run(download_page("https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP"))
    assert "Natural language processing (NLP) is the ability of a computer program to understand human language" in page_content and \
        "</span>" not in page_content

