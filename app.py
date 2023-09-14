from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/channels")
def channels():
    return "<p>Channels: None, i have no channels</p>"