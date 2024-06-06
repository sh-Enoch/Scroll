from . import models
from . import app
from setup import *


def get_genres():
    with app.app_context():
        return models.Genre.query.all()

def get_books():
    with app.app_context():
        return models.Book.query.all()

def all_users():
    with app.app_context():
        return models.User.query.all()

#print(all_users())
#print(get_books())
#print(get_genres())

def show_cover_image():
    with app.app_context():

        return models.Book.query.filter_by(id=1).first().cover_image
    

print(show_cover_image())