import requests
import json
from IPython.display import HTML

key1 = "4984af63239647179cc7489cfdf1771f"
key2 = "7459a42c4b0a493ba17d74296af2d236"
search_url = "https://api.bing.microsoft.com/v7.0/search"
search_term = "dogs"

headers = {"Ocp-Apim-Subscription-Key": key1}
params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

search_results = json.dumps(search_results, indent=2)

with open("../outputs/bing_results.json", "w") as file:
    file.write(search_results)
