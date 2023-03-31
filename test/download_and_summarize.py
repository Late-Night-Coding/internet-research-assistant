# This was written before any test frameworks were added. Feel free to modify it to incorporate a framework

import asyncio

from nlp.basic_summarizer import basic_summarize
from searches.webpage_downloader import download_page


url = "https://simple.wikipedia.org/wiki/Pok%C3%A9mon"
page_content = asyncio.run(download_page(url))  # important: note that the call is async
summary = basic_summarize(page_content)
print(summary)
