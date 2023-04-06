class SearchHistory:
    def __init__(self, firstKeyword, id):
        self.id = id
        self.keywordList = [firstKeyword]
    
    def appendKeywords(self, keywords):
        self.keywordList.append(keywords)

    def getKeywordsList(self):
        return self.keywordList