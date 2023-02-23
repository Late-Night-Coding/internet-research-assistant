from googlesearch import search as googleSearch


def search(query, num, stop, pause):

    tld = "co.in"
    results = googleSearch(query, tld, num=num, stop=stop, pause=pause)

    return results
