from googlesearch import search as googleSearch


class Google:

    def __init__(self):
        self.results = list()

    def search(self, query, num, stop, pause):
        tld = "co.in"
        self.results = googleSearch(query, tld, num=num, stop=stop, pause=pause)

        return self.results

    def get_results(self, size=100):
        if size > len(self.results):
            return self.results
        else:
            return self.results[:size]
