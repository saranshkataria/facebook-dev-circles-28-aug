from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from app import views, models


@app.route('/')
def home():


@app.route('/login')
def login():


@app.route('/logout')
def logout():


@app.route('/event/<id>')
def event():


@app.route('/event/<id>/query')
def query():


@app.route('/event/<id>/import_csv')
def import_csv():


@app.route('/event/<id>/attendees')
def attendees():


@app.route('/event/<id>/send_invite')
def send_invite():


@app.route('/event/<id>/edit')
def edit():


@app.route('/event/<id>/stats')
def stats():


@app.route('/validate_qr')
def validate_qr():

if __name__ == "__main__":
    app.run(debug=True)
