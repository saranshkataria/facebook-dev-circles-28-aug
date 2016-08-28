from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

from app import views, models

if __name__ == "__main__":
    app.run(debug=True)