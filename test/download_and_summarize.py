# This was written before any test frameworks were added. Feel free to modify it to incorporate a framework

import asyncio

from nlp.basic_summarizer import basic_summarize
from searches.webpage_downloader import download_page
from searches.bing_search import Bing
from searches.openai_search import OpenAI
from searches.google_search import Google



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

    links = list()

    for item in results:
        if isWiki(item):
            links.append(item)

    print(links)
    total_summary = ""

    for url in links:
        print(url)
        page_content = asyncio.run(download_page(url))  # important: note that the call is async
        summary = basic_summarize(page_content)
        print(summary)
        total_summary = total_summary + summary

    print("\n" + total_summary + "\n")

    openai = OpenAI()
    response = asyncio.run(openai.summarize(total_summary))
    print(response)

def isWiki(link):
    link = link.lower().split(".")
    for part in link[:-1]:
        if ("wiki" in part or "fandom" in part) or ("britannica" in part or "pedia" in part):
            return True

    return False

if __name__ == "__main__":
    main()
