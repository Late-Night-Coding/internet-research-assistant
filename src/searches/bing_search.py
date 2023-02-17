import requests
import json
import os
import src.file_io as file_io

key1 = "a545213acdb4407c9f3fffc6097f9b67"
key2 = "ebf8de5d4f9240ea9911a24d2c25d9d9"
search_url = "https://api.bing.microsoft.com/v7.0/search"
search_term = "cats"

headers = {"Ocp-Apim-Subscription-Key": key1}
params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

search_results = json.dumps(search_results, indent=2)

with file_io.write_file("test.json") as file:
    file.write(search_results)
