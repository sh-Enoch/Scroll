from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)

class Journals(Base):
    __tablename = 'journals'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    editor = Column(String)
    topic = Column(String)

class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String)
    author_email = Column(String)
    author_book = Column(String)
    author_bio = Column(String)
    nationality =  Column(String)
    relationship('Book', backref='author')

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement= True)
    user_name = Column(String)
    user_email = Column(String)
    user_password =  Column(unique=True)

class Genre(Base):
    __tablename__ = 'genre'
    genre_id = Column(Integer, primary_key=True, autoincrement=True)
    genre_name = Column(String)
    genre_books = Column(Integer, ForeignKey('books.id')) #foreign key  references book_id

class Downloads(Base):
    __tablename__ = 'downloads'
    download_id = Column(Integer, primary_key=True, autoincrement=True)
    download_content = Column(Integer, ForeignKey('books.id')) #foreign key references book downloaded
    download_user_id = Column(Integer, ForeignKey('users.user_id')) #foreign key references user downloading the book.
    download_date = Column(DateTime)

class UserBooks(Base):
    __tablename__ = 'user_books'
    user_book_id = Column(Integer,primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id')) #foreign key references book 
    read_status = Column(String)
    read_timestamp = Column(DateTime)

class Reviews(Base):
    __tablename__ = 'Reviews'
    review_id = Column(Integer, autoincrement=True)
    review_user_id = Column(Integer, ForeignKey('users.user_id')) #foreign key references the user_id from users
    rating = Column(Integer)
    comment = Column(String)