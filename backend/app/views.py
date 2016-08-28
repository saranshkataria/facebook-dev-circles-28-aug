from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from app import views, models


@app.route('/')
def home():
    pass

@app.route('/register')
def register():
    pass

@app.route('/login')
def login():
    pass

@app.route('/logout')
def logout():
    pass

@app.route('/event/<id>')
def event():
    pass

@app.route('/event/<id>/query')
def query():
    pass

@app.route('/event/<id>/import_csv')
def import_csv():
    pass

@app.route('/event/<id>/attendees')
def attendees():

@app.route('/event/<id>/attendees/add_walkin')
def add_walkin():
    pass

@app.route('/event/<id>/send_invite')
def send_invite():
    pass

@app.route('/event/<id>/edit')
def edit():
    pass

@app.route('/event/<id>/stats')
def stats():
    pass

@app.route('/validate_qr')
def validate_qr():
    pass

if __name__ == "__main__":
    app.run(debug=True)
