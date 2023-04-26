import asyncio
from data.topic_results import TopicResults
from data.research_results import ResearchResults
from web_search.search_aggregator import SearchAggregator
from topic_summarizer import TopicSummarizer

class SearchProcessor:
    def __init__(self) -> None:
        self.search_aggregator = SearchAggregator()
        self.topic_summarizer = TopicSummarizer()

    async def search(self, keywords: list[str], summary_len:int) -> ResearchResults:

        # Create ResearchResult object
        research_results = ResearchResults()

        # Create tasks for each keyword to search asynchronously
        tasks: list[asyncio.Task[TopicResults]] = []
        for keyword in keywords:
            task = asyncio.create_task(self.__search_keyword(keyword, summary_len))
            tasks.append(task)

        # Gather the results of all tasks
        topics: list[TopicResults] = await asyncio.gather(*tasks)

        # Process the responses and add them to the results list
        for topic in topics:
            if topic:
                research_results.add_topic(topic)

        return research_results

    async def __search_keyword(self, keyword, summary_len: int) -> TopicResults:
        # use search engines to obtain urls relating to the keyword
        links = await self.search_aggregator.search(keyword)

        # Obtain summary from links
        topic_info = await self.topic_summarizer.summarize_topic(links, keyword, summary_len)

        return topic_info
