from googlesearch import search

# to search
query = "Geeksforgeeks"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
