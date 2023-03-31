from flask import Flask, render_template, request

app = Flask(__name__)

def get_results(query):
    # TODO: This is a dummy function. Implement it later
    return [
        {
            "title": "Sport",
            "description": "Baseball is a bat-and-ball sport between two teams of nine players each, taking turns batting and fielding.",
            "links": [
                {"url": "https://wikiexample0.com/", "link_hue": "28", "link_type": "Wiki", "name": "Wiki Link 1"},
                {"url": "https://wikiexample2.com/", "link_hue": "28", "link_type": "Wiki", "name": "Wiki Link 2"},
                {"url": "https://youtube.com/", "link_hue": "0", "link_type": "Youtube", "name": "Youtube Link 1"},
                {"url": "https://otherexample.com/", "link_hue": "186", "link_type": "Other", "name": "Other Link 1"}
            ],
            "reason": "This was the first item returned by google search" 
        },
        {
            "title": "Pitching",
            "description": "Pitching is a fundamental aspect of baseball, and it's important to understand the different types of pitches that pitchers can throw in order to effectively analyze and appreciate the game.",
            "links": [
                {"url": "https://wikiexample0.com/", "link_hue": "28", "link_type": "Wiki", "name": "Wiki Link 1"},
                {"url": "https://wikiexample2.com/", "link_hue": "28", "link_type": "Wiki", "name": "Wiki Link 2"},
                {"url": "https://youtube.com/", "link_hue": "0", "link_type": "Youtube", "name": "Youtube Link 1"},
                {"url": "https://otherexample.com/", "link_hue": "186", "link_type": "Other", "name": "Other Link 1"}

            ],
            "reason": "This was the first item returned by bing search" 
        },
        {
            "title": "MLB",
            "description": "Major League Baseball (MLB) is a professional baseball organization and the oldest major professional sports league in the world.",
            "links": [
                {"url": "https://wikiexample0.com/", "link_hue": "28", "link_type": "Wiki", "name": "Wiki Link 1"},
                {"url": "https://wikiexample2.com/", "link_hue": "28", "link_type": "Wiki", "name": "Wiki Link 2"},
                {"url": "https://youtube.com/", "link_hue": "0", "link_type": "Youtube", "name": "Youtube Link 1"},
                {"url": "https://otherexample.com/", "link_hue": "186", "link_type": "Other", "name": "Other Link 1"}

            ],
            "reason": "This was the second item returned by google search" 
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
