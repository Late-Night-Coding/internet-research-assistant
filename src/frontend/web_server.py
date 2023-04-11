import asyncio
import time
from async_util import get_event_loop
import search_controller
from flask import Flask, render_template, request

app = Flask(__name__)


def get_results(query):
    start_time = time.time()
    searcher = search_controller.SearchController()
    result, search_id = get_event_loop().run_until_complete(searcher.search(query))
    result_list = []
    for topic in result.topics:
        link_list = []
        for url in topic.url_list:
            link_list.append({
                "url": url.link,
                "link_hue": str(url.category.color),
                "link_type": url.category.name,
                "name": url.name  # You may want to add a name attribute to URL class and retrieve it here
            })
        result_list.append({
            "title": topic.topic_name,
            "description": topic.topic_description,
            "links": link_list
        })

        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
    return result_list


@app.route('/')
def homepage():
    """This function is called by flask every time a user visits the homepage.
    Look inside the `frontend/templates/homepage.html` file to see the content that is rendered.
    """
    return render_template('homepage.html')


@app.route("/search")
def search():
    """Called on each search query"""

    search_query = request.args.get('query').strip()
    print("got " + search_query + " from html")

    # TODO: handle requests asynchronously (async / await)
    results = get_results(search_query)

    return render_template('search.html', results=results, query=search_query)


# Entry point
def start():
    app.run(host="0.0.0.0", port=8080)


if __name__ == '__main__':
    start()
