import requests
import json
import os
import src.file_io as file_io



class Bing:

    def __init__(self):
        self.key1 = "a545213acdb4407c9f3fffc6097f9b67"
        self.key2 = "ebf8de5d4f9240ea9911a24d2c25d9d9"
        self.search_url = "https://api.bing.microsoft.com/v7.0/search"
        self.headers = {"Ocp-Apim-Subscription-Key": self.key1}

    def search(self, search_term, count=10):
        params = {"q": search_term, "textDecorations": True, "textFormat": "HTML", "count": count, "responseFilter": "Webpages"}

        response = requests.get(self.search_url, headers=self.headers, params=params)
        response.raise_for_status()
        search_results = response.json()

        search_results = [page["url"] for page in search_results["webPages"]["value"]]

        return search_results
