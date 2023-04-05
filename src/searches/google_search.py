from googlesearch import search as googleSearch


async def search(query, num=10, stop=None, pause=2):
    tld = "co.in"
    results = googleSearch(query, tld, num=num, stop=stop, pause=pause)
    return [link for link in results]

