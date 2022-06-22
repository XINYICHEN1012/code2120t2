from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, I am Shandy from UNSW CODE2120 </p>"
