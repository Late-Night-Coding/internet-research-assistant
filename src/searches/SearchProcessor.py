import asyncio
from ResearchResults import ResearchResults
from nlp.basic_summarizer import basic_summarize
from searches.webpage_downloader import download_page
from google_search import search as googleSearch
from bing_search import Bing
from chatGPT import generate_chat_response as GPTDescritpion 
#from ResearchResults import addTopics  

class SearchProcessor:
    async def search(self, keywords):
        
        #Create ResearchResult obj
        research_results = ResearchResults()

        # Create a list to store the results
        results = []

        # Create tasks for each keyword to search asynchronously
        tasks = []
        for keyword in keywords:
            task = asyncio.ensure_future(self.search_keyword(keyword))
            tasks.append(task)

        # Gather the results of all tasks
        responses = await asyncio.gather(*tasks)
 
        # Process the responses and add them to the results list
        for response in responses:
            if response:
                print(response[0])
                print(response[1])
                print(response[2])
                research_results.addTopics(response[0],response[1],response[2])
                results.append(response)         
                
        # Return the ResearchResults object with the compiled results
        return research_results
    


    async def search_keyword(self, keyword):
        # Perform Google search for the given keyword asynchronously
        print(f"Google search for keyword: {keyword}")
        google_urls = await self.retrieve_google_urls(keyword)
        
        # Perform Bing search for the given keyword asynchronously
        print(f"Bing search for keyword: {keyword}")
        bing_urls = await self.retrieve_bing_urls(keyword)

        # Combine the list of URLs from Google and Bing searches
        urls = google_urls + bing_urls

        # Download and summarize pages for ChatGPT
        summaries = []
        for url in urls:
            summary = await basic_summarize(url)
            summaries.append(summary)

        # Query ChatGPT for descriptions using the keyword and summarized content
        descriptions = await self.query_gpt(keyword, summaries)
        topic_info = [keyword,descriptions,urls]

        # Combine the results of each keyword's thread
        return topic_info
        
       

    async def retrieve_google_urls(self, keyword):
        query = keyword
        num = 10
        stop = 5
        pause = 2
        # Call the search function
        results = await googleSearch(query, num, stop, pause)

        return list(results)

    async def retrieve_bing_urls(self, keyword):
       
        # Call the search function with a search term
        bing = Bing()
        query = keyword
        count = 10 
        results = await bing.search(query, count)
        # Return the search results
        return list(results)
        

    async def query_gpt(self, keyword, summaries):
        prompt = f"User is doing research on {keyword}. The content of website says {summaries} ... . Provide a description for {keyword} " 
        response = GPTDescritpion(prompt)
        return response



# driver code for testing 
async def main():
    keywords = ["cats", "dogs"]  
    search_processor = SearchProcessor()
    results = await search_processor.search(keywords)
    


loop = asyncio.get_event_loop()
loop.run_until_complete(main())