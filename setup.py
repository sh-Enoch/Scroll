# setup.py
from frontend import  app  # assuming 'app' is your Flask application instance
from frontend.models import db
from  frontend.models import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b84ec431597ecc1b44d18c7a5c2edc3d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://syncthia:mylovelypc@localhost/scrolls'

db.init_app(app)

#with app.app_context():
    #db.create_all()
#
    #db.session.add(genre1)
    #db.session.add(genre2)
    #db.session.add(genre3)
    #db.session.commit()
#
    #db.session.add(book1)
    #db.session.add(book2)
    #db.session.add(book3)
    #db.session.add(book4)
#
    #db.session.add(book6)
    #db.session.add(book7)
    #db.session.add(book8)
#
    #db.session.add(book9)
    #db.session.add(book10)
    #db.session.add(book11)
#
    #db.session.commit()
