from flask import Flask, render_template, url_for, request, redirect,jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import json

from pip import main
from main import table

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
db = SQLAlchemy(app)

display = ["Name: ", "Money: ", "Card 1: ", "Card 2: ", "Current bid: "]


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    money = db.Column(db.Integer, default=0)
    Card_1 = db.Column(db.String)
    Card_2 = db.Column(db.String)
    current_bid = db.Column(db.Integer, default=0)
    still_in = db.Column(db.Boolean, default=True)
           
class Game(Resource):
    def get(self):
        return jsonify(cards=table)

api.add_resource(Game, '/table')

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    main
