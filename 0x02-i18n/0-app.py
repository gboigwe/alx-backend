#!/usr/bin/env python3
"""Creating a basic flask app"""


from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")

@app.route("/", method=["GET"], strict_slashes=False)
def hello_world():
    """Rendering the template for the flask"""
    return tender_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
