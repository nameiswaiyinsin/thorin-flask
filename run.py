import os
from flask import Flask, render_template


app = Flask(__name__)          #an instance of flask class and stored in variable called 'app'


@app.route("/")                #using the app.route decorator (@) also called pi notation, will be used to wrap functions as all functions are objects and can be passed around. When we try to browse to the root directory ("/"), the flask triggers the index() function and returns the hello world text.
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True)           # debug = True should never be in a production project or when we submit for our assignments, it is a security flaw because it allows arbitrary codes to run. It can only be used in development stage of project. Change it to debug = False before submitting project.


