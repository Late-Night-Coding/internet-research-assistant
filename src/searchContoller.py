import asyncio
from searches.openai_search import OpenAI
import searches.google_search as google
from searches.bing_search import Bing
import flask

from searches.Search import Search
from searches.SearchHistory import SearchHistory
from nlp.input_parser import Input_Parser

class SearchController:
    def __init__(self):
        self.searchObject = Search()
        self.inputParser = Input_Parser()
        #query = "iasubyaseiruntgiuaydhfbi auhergi uhaedfkbn wiertuh skdjhn wseirtuyh df "
        #self.bingSearcher = Bing()
        #response = self.bingSearcher.search(query)
        #print(response)
        
        #response = asyncio.run(google.search(query, 10, 10, 10))
        #print(response)
        #openai = OpenAI()
        #response = openai.chat("what are some categories for the following phrase: Pokemon")
        #print(response)
    
    async def search(self, query, id=None):
        results = None
        extendedQueryString = ""

        #if id==None -> a whole new searcj
        if(id == None):
            self.searchHistory = SearchHistory(query, 0)
            currentKeyWordinHistory = query

        #this section might become a pain to figure out
        else:
            currentKeyWordinHistory = self.searchHistory.getKeywordsList[id]

        #gets the list of queries on top of each other
        extendedQueryList = self.inputParser.parseInput(query, currentKeyWordinHistory)
        print(extendedQueryList)

        #convert the list of queries into a sentence/string
        for query in extendedQueryList:
            extendedQueryString += ' '+query

        results = await(self.searchObject.search(extendedQueryString))
        print(results)
        return results #for now returns a 2d array of searches from Bing and Google

if __name__ == "__main__":
    main = SearchController()
    asyncio.run(main.search("Baseball"))