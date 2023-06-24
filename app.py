import os.path
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__, template="templates")


@app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
