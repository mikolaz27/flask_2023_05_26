from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello_mykhailo():
    # view
    return "<p>Hello, Mykhailo!</p>"


@app.route("/now")
def get_datetime():
    return f"current time: {datetime.datetime.now()}"


app.run(port=5001, debug=True)
