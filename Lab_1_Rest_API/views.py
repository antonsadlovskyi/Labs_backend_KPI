from Lab_1_Rest_API import app


@app.route("/")
def helloWorld():
    return "Hello World!"
