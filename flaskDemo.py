

from flask import Flask, make_response
from flask_wtf import FlaskForm
import json

app = Flask(__name__)


@app.route("/")
def index():
    data = {
        "name": "python",
        "age": 18
    }
    json_str = json.dumps(data)

    return json_str


if __name__ == '__main__':
    app.run()