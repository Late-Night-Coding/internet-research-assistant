from flask import Flask, render_template, request

app = Flask(__name__)

def get_results(query):
    # TODO: This is a dummy function. Implement it later
    return [
        {
            "title": "Result 1",
            "text": f"This is the first result for {query}"
        },
        {
            "title": "Result 2",
            "text": f"This is the second result for {query}"
        },
    ]


@app.route('/')
def homepage():
    """This function is called by flask every time a user visits the homepage.
    Look inside the `frontend/templates/homepage.html` file to see the content that is rendered.
    """
    return render_template('homepage.html')

@app.route("/search")
def search():
    """Called on each search query"""

    search_query = request.args.get('query') 

    # TODO: handle requests asynchronously (async / await)
    results = get_results(search_query)

    return render_template('search.html', results=results, query=search_query)


# Entry point
def start():
    app.run(host="0.0.0.0", port=8080)

if __name__ == '__main__':
    start()