from searches.openai_search import OpenAI
from searches.google_search import Google
import flask


class SearchController:
    def __init__(self):
        self.openai = OpenAI()
        response = self.openai.chat('find related topics for this phrase: "linearly independent vectors"')
        print(response)


if __name__ == "__main__":
    main = SearchController()