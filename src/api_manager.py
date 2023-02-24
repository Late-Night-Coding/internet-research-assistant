
from searches.openai_search import OpenAI
import flask


class API_Manager:
    def __init__(self):
        self.openai = OpenAI()
        response = self.openai.chat("hi")
        print(response)



if __name__ == "__main__":
    main = API_Manager()