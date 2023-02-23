from searches import google_search


def main():

    results = google_search.search("dog", 10, 50, 2)


    for result in results:
        print(result)



if __name__ == "__main__":
    main()