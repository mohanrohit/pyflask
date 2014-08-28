from app import app

from flask import render_template

@app.route("/")
@app.route("/hello/1/0")
@app.route("/hello-1.0")
def hello_1_0():
    return "Hello World"

@app.route("/hello/1/1")
@app.route("/hello-1.1")
def hello_1_1():
    return render_template("hello-1.1.html")
