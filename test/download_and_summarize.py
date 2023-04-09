# This was written before any test frameworks were added. Feel free to modify it to incorporate a framework

import asyncio
import os
from nlp.basic_summarizer import basic_summarize
from openai_api import OpenAI
from web_search.bing_search import Bing
from web_search.google_search import Google
from web_search.webpage_downloader import download_page



def main():
    # only set event loop policy for windows
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    bing_searcher = Bing()
    google_search = Google()
    query = "pokemon types"
    results = asyncio.run(bing_searcher.search(query, count=20))
    result_google = asyncio.run(google_search.search(query, count=20))
    results.extend(result_google)

    print(results)

    wikiLinks = list()

    for item in results:
        if isWiki(item):
            wikiLinks.append(item)

    print(wikiLinks)
    total_summary = ""

    for url in wikiLinks:
        print(url)
        page_content = asyncio.run(download_page(url))  # important: note that the call is async
        summary = basic_summarize(page_content)
        print(summary)
        total_summary = total_summary + summary

    print("total Summary:")
    print("\n" + total_summary + "\n")

    # openai = OpenAI()
    # response = asyncio.run(openai.summarize(total_summary))
    # print(response)

def isWiki(link):
    link = link.lower().split(".")
    for part in link[:-1]:
        if ("wiki" in part or "fandom" in part) or ("britannica" in part or "pedia" in part):
            return True

    return False

if __name__ == "__main__":
    main()
