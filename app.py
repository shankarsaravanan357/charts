from re import X
from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, make_response


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///randomvalues.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'abcdefgh'

db = SQLAlchemy(app)

class Randomvalues(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    ranval = db.Column(db.Float)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    args = request.args.get('name')
    print (args) # For debugging
    print("helo")
    value1 = Randomvalues.query.filter_by(id = args).first()
    data = [time() * 1000, value1.ranval]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


if __name__ == "__main__":
    app.run(debug=True)