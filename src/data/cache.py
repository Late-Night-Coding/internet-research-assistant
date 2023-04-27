import os
import pickle


class Cache:
    def __init__(self):
        # save the cache folder and if there is no cache folder, then make one
        self.CACHE_FOLDER = os.path.join(os.getcwd(), "data", "cache")
        if not os.path.exists(self.CACHE_FOLDER):
            os.makedirs(self.CACHE_FOLDER)

    def cache(self, query, data):
        file_path = os.path.join(self.CACHE_FOLDER, query + ".pickle")
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
    
    
    def isCached(self, query) -> bool:
        file = os.path.join(self.CACHE_FOLDER, query + ".pickle")
        if os.path.exists(file):
            return True
        return False
    
    
    def getCache(self, query) -> dict:
        data = None
        file = os.path.join(self.CACHE_FOLDER, query + ".pickle")
        if os.path.exists(file):
            with open(file, "rb") as file:
                data = pickle.load(file)
        return data

