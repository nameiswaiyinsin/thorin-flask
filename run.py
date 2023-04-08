import os
from flask import Flask


app = Flask(__name__)          #an instance of flask class and stored in variable called 'app'


@app.route("/")                #using the app.route decorator (@) also called pi notation, will be used to wrap functions as all functions are objects and can be passed around. When we try to browse to the root directory ("/"), the flask triggers the index() function and returns the hello world text.
def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True)