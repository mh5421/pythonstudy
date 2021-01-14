from flask import Flask, render_template,jsonify, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime


__all__ = ['app']

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

from service import *

@app.route("/")
def hello():
    return render_template('board.html')

if __name__ == "__main__":
    app.run(debug=True)