import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)          #an instance of flask class and stored in variable called 'app'
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")                #using the app.route decorator (@) also called pi notation, will be used to wrap functions as all functions are objects and can be passed around. When we try to browse to the root directory ("/"), the flask triggers the index() function and returns the hello world text.
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)           # debug = True should never be in a production project or when we submit for our assignments, it is a security flaw because it allows arbitrary codes to run. It can only be used in development stage of project. Change it to debug = False before submitting project.


