class SearchHistory:
    def __init__(self, first_keyword: str, id: str):
        self.id = id
        self.keyword_history = [first_keyword]
    
    def append_keyword(self, keyword: str):
        self.keyword_history.append(keyword)

    def get_keyword_history(self):
        return self.keyword_history

    def __str__(self) -> str:
        return " > ".join(self.keyword_history)