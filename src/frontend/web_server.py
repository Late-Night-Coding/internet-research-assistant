import asyncio
import time
from async_util import get_event_loop
from data.research_results import ResearchResults
from data.search_history import SearchHistory
from dummy_search_controller import get_dummy_search_controller
import search_controller
from flask import Flask, render_template, request, abort

app = Flask(__name__)

# searcher = search_controller.SearchController()
searcher = get_dummy_search_controller()

def get_results(query, search_id=None) -> tuple[ResearchResults, SearchHistory]:
    start_time = time.time()

    # run the async search function synchronously
    result, search_history = get_event_loop().run_until_complete(searcher.search(query, search_id))

    # force typing
    result: ResearchResults
    search_history: SearchHistory

    # create the topic for flask
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

    return result_list, search_history


@app.route('/')
def homepage():
    """This function is called by flask every time a user visits the homepage.
    Look inside the `frontend/templates/homepage.html` file to see the content that is rendered.
    """
    return render_template('homepage.html', id=None)


@app.route("/search")
def search():
    """Called on each search query"""

    # extract (query, id) from url arguments
    args = request.args
    search_query = args.get('query').strip()
    search_id = args.get('id', None) or None
    try:
        # TODO: handle requests asynchronously (async / await)
        results, search_history = get_results(search_query, search_id)
    except asyncio.exceptions.TimeoutError:
        abort(504)

    return render_template(
        template_name_or_list='search.html',
        results=results,
        query=search_query,
        id=search_history.id,
        history=search_history.get_keyword_history()
    )

@app.errorhandler(504)
def errorTimeout(error):
    print(str(error))
    error_code = "504"
    error_message = "Looks like OpenAI took too long getting back to us. Please head back to the main screen and try again"
    return render_template(
        template_name_or_list='error.html',
        error_code=error_code,
        error_message=error_message), 504

# Entry point
def start():
    app.run(host="0.0.0.0", port=8080)


if __name__ == '__main__':
    start()
