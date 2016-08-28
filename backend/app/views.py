from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import hashlib
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from app.models import User


@app.route('/register')
def register():
	parser = reqparse.RequestParser()
	parser.add_argument('email', type=str)
	parser.add_argument('token', type=str)
	args = parser.parse_args()
	email = args['email']
	token = args['token']
	password = hashlib.md5(token.encode())
	user = User.query.filter_by(email = email)
	if user:
		return jsonify(user.password)
	else :
		user  = User(email = email , password = password)
		db.session.add(user)
		db.session.commit()
	return jsonify(password)

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
