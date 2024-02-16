from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "h"
@app.route("/about")
def about():
    return "efsd"