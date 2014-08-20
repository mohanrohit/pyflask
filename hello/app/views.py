from app import app

@app.route("/hello-1.0")
def hello_1_0():
    return "Hello World"
