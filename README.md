# internet-research-assistant

## Setup
Project dependencies in this branch are managed using [poetry](https://python-poetry.org/docs/). Complete setup instructions are given below.

Before getting started, make sure a recent version of python and pip are installed on your system. Then run these commands:

1. Clone & open this github repo:
```bash
git clone https://github.com/ptrpham1234/internet-research-assistant.git
# Or use your preferred git client

cd internet-research-assistant
```

2. Install poetry
```bash
pip install poetry
```

3. Install packages
```bash
poetry install
```

4. Test it out
```bash
poetry shell    # <- THIS IS IMPORTANT: Enter the project's virtual environment first
python src/searches/google_search.py
```
If there are dependency errors try the command bellow:
```bash
poetry run python src/searches/google_search.py
```

### VS Code Setup
After completing the above, you can get this project working in VS Code by following these stesps:

1. Open this project directory in VS Code
2. Ensure the official [Python VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) is installed
3. Press `Ctrl+Shift+P` and enter the command `Python: Select Interpreter`
4. Select  `Python 3.x.x (internet-research-assistant-xxxxxx)`
5. Open a python file to run. Go into the `Run and Debug` menu, then press `Python: Current file`

## Running the web server
To launch the web server locally, type these commands in the project directory:
```bash
poetry install          # to ensure packages are up to date
poetry run webserver
```
Then you can open up http://localhost:8080 to see it up and running