# setup.py
from frontend import  app  # assuming 'app' is your Flask application instance
from frontend.models import db
from  frontend.models import User
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b84ec431597ecc1b44d18c7a5c2edc3d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://syncthia:mylovelypc@localhost/scrolls'

db.init_app(app)

with app.app_context():
    db.create_all()