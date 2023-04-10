import asyncio
from nlp.basic_summarizer import basic_summarize
from data.research_results import ResearchResults
from openai_api import OpenAI
from web_search.search_aggregator import SearchAggregator
from web_search.webpage_downloader import download_page
from data.web_content import WebContent


#############################################################################################################
#  * Function:            __is_wiki_link__
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        04/05/2023

#  * Description:
#  * Returns a bool value if the link provided is a wiki.
#  *

#  * Parameters:
#  * link               list()              link to analyze
#############################################################################################################
def __is_wiki_link__(link: str):
    link = link.lower().split(".")
    for part in link[:-1]:
        if ("wiki" in part or "fandom" in part) or ("britannica" in part or "pedia" in part):
            return True

    return False


#############################################################################################################
#  * Function:            summarize_topic
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        03/28/2023

#  * Description:
#  * Returns a summary/description of a topic given the links. It will only summarize wiki links due to length
#  * and api limitations. the links should be the same or of similar topic or the summary not be focused.

#  * Parameters:
#  * links              list()              list of all the links to summarize
#############################################################################################################
async def summarize_topic(links: list[str], keyword: str) -> tuple:
    wiki_links = set()
    web_pages = list()

    wiki_links = list(wiki_links)



    total_summary = ""

    tasks = []

    # summarizes each link and consolidate them together
    print("downloading page contents for each links")
    for url in links:
        task = asyncio.create_task(download_page(url))
        tasks.append(task)

    web_pages = await asyncio.gather(*tasks)


    for page in web_pages:
        if __is_wiki_link__(page.url):
            wiki_links.append(page)

    # limit the number of links
    # TODO: Maybe change this limit
    if len(wiki_links) > 3:
        wiki_links = wiki_links[:3]

    for page in wiki_links:
        summary = basic_summarize(page.content, [keyword])
        total_summary = total_summary + summary

    openai = OpenAI()
    response = await openai.summarize(keyword, total_summary)

    return response, web_pages


class SearchProcessor:
    def __init__(self) -> None:
        self.search_aggregator = SearchAggregator()

    async def search(self, keywords: list[str]):

        # Create ResearchResult obj
        research_results = ResearchResults()

        # Create tasks for each keyword to search asynchronously
        tasks = []
        for keyword in keywords:
            task = asyncio.create_task(self.__search_keyword(keyword))
            tasks.append(task)

        # Gather the results of all tasks
        responses = await asyncio.gather(*tasks)

        # Process the responses and add them to the results list
        for response in responses:
            if response:
                research_results.add_topic(response[0], response[1], response[2], response[3])

        return research_results

    async def __search_keyword(self, keyword):
        # use search engines to obtain urls relating to keyword
        urls = await self.search_aggregator.search(keyword)

        # Obtain summary from links
        print("starting topic summarization")
        summary, page_contents = await summarize_topic(urls, keyword)
        print("finished topic summarization")
        topic_info = [keyword, summary, urls, page_contents]

        # Combine the results of each keyword's thread
        return topic_info
