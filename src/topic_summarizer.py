import asyncio

from data.topic_results import TopicResults
from data.url import create_url_from_web_content
from data.web_content import WebContent

# Service Dependencies
from nlp.basic_summarizer import basic_summarize
from openai_api import OpenAI
from web_search.webpage_downloader import download_page

class TopicSummarizer:

    def __init__(self) -> None:
        # I declare these as variables here so that they can be substituted by mock services in tests
        self.open_ai = OpenAI()
        self.summarize_page_content_fn = basic_summarize
        self.download_page_fn = download_page

    #############################################################################################################
    #  * Function:            __is_wiki_link
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        04/05/2023

    #  * Description:
    #  * Returns a bool value if the link provided is a wiki.
    #  *

    #  * Parameters:
    #  * link               list()              link to analyze
    #############################################################################################################
    def __is_wiki_link(self, link: str):
        link = link.lower().split(".")
        for part in link[:-1]:
            if ("wiki" in part or "fandom" in part) or ("britannica" in part or "pedia" in part):
                return True

        return False
    
    def __limit_links(self, links: list[str]):
        """Take a set of links, and limit the number of pages that are downloaded"""

        # prioritize wiki links
        wiki_links : list[str] = []
        non_wiki_links : list[str] = []
        for link in links:
            if self.__is_wiki_link(link):
                wiki_links.append(link)
            else:
                non_wiki_links.append(link)
        
        # limit to 5 + 10 = 15 total links
        if len(wiki_links) > 5:
            wiki_links = wiki_links[:5]
        
        if len(non_wiki_links) > 10:
            non_wiki_links = non_wiki_links[:10]
        
        return [*wiki_links, *non_wiki_links]

    
    async def __download_all_pages(self, links: list[str]) -> list[WebContent]:
        """Download multiple pages on different threads. Combine them all into a list and return"""

        # Ensure links are unique. Preserve their order
        seen_links: set[str] = set()
        unique_links: list[str] = []
        for link in links:
            if link not in seen_links:
                unique_links.append(link)
                seen_links.add(link)

        # Download all the pages
        download_tasks: list[asyncio.Task[WebContent]] = []
        for url in links:
            task = asyncio.create_task(self.download_page_fn(url))
            download_tasks.append(task)
        web_pages: list[WebContent] = await asyncio.gather(*download_tasks)

        return web_pages
    
    async def __get_description_from_pages(self, keyword: str, web_pages: list[WebContent], summary_len: int) -> str:
        """Given a keyword and a list of downloaded web pages, filter the wiki pages, and return an appropriate summary for the keyword"""

        # Filter for wiki pages only
        wiki_pages = [
            page for page in web_pages
            if self.__is_wiki_link(page.url)
        ]

        # Limit to 3 pages
        if len(wiki_pages) > 3:
            wiki_pages = wiki_pages[:3]

        # summarizes each wiki page and consolidate them together
        all_summaries = ""
        for page in wiki_pages:
            all_summaries += self.summarize_page_content_fn(page.content, [keyword])

        # use openai to summarize the consolidated summaries
        return await self.open_ai.summarize(keyword, all_summaries, summary_len)


    #############################################################################################################
    #  * Function:            summarize_topic
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        03/28/2023

    #  * Description:
    #  * Returns the TopicResults of a topic given the links the keyword. It will only summarize wiki links due to length
    #  * and api limitations. the links should be the same or of similar topic or the summary not be focused.

    #  * Parameters:
    #  * links              list()              list of all the links to summarize
    #############################################################################################################
    async def summarize_topic(self, links: list[str], keyword: str, summary_len: int) -> TopicResults:

        # To avoid downloading too much, limit the number of total links we download.
        links = self.__limit_links(links)

        # Download all the pages
        web_pages = await self.__download_all_pages(links)

        # Get the topic description from the web pages
        topic_description = await self.__get_description_from_pages(keyword, web_pages, summary_len)

        # create URL objects
        urls = [
            create_url_from_web_content(page)
            for page in web_pages
        ]

        return TopicResults(
            topic_name=keyword,
            topic_description=topic_description,
            url_list = urls
        )
