from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.String(length=30), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


@app.route('/') #decorator
@app.route('/home') #decorator
def home_page():
    return render_template('home.html')

@app.route('/about/<username>') #dynatic route can recieve an username or any other string
def about_page(username):
    return '<h1>This is the about page of {username}</h1>'

@app.route('/market')
def market_page():
    items = [
        {'name': 'Phone', 'price': 500, 'quantity': 10},
        {'name': 'Laptop', 'price': 1000, 'quantity': 5},
        {'name': 'Tablet', 'price': 300, 'quantity': 8},
    ]
    return render_template('market.html',item_name= items)