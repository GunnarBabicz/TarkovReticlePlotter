from flask import Flask

app = Flask(__name__) # instantiating the flask app object

@app.route("/")
def index():
    return "Hello World"