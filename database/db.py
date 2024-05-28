from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)

class Magazines(Base):
    __tablename__ = 'magazines'
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    editor = Column(String)
    topic = Column(String)

class Newspapers(Base):
    __tablename__ = 'newspapers'
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    editor = Column(String)
    topic = Column(String)



class Journals(Base):
    __tablename = 'journals'
    book_id =  Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    editor = Column(String)
    topic = Column(String)
 
class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String)
    author_email = Column(String)
    book_id= Column(String, ForeignKey('books.id'))
    author_bio = Column(String)
    nationality =  Column(String)
    books = relationship('Book', backref='author')

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
    books = relationship('Book', secondary='genre_books', back_populates='genre')
class Downloads(Base):
    __tablename__ = 'downloads'
    download_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id')) #foreign key references book downloaded
    user_id = Column(Integer, ForeignKey('users.user_id')) #foreign key references user downloading the book.
    download_date = Column(DateTime)
    book = relationship('Book', backref='downloads')

class UserBooks(Base):
    __tablename__ = 'user_books'
    user_book_id = Column(Integer,primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id')) #foreign key references book 
    read_status = Column(String)
    read_timestamp = Column(DateTime)

    user = relationship('Users', backref='user_books')

class Reviews(Base):
    __tablename__ = 'Reviews'
    review_id = Column(Integer, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id')) #foreign key references the user_id from users
    book_id = Column(Integer, ForeignKey('books.id')) #foreign key references the book_id from books
    rating = Column(Integer)
    comment = Column(String)

    user = relationship('Users', backref='reviews')
    book = relationship('Book', backref='reviews')

class UserBookmarks(Base):
    __tablename__ = 'user_bookmarks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    timestamp = Column(DateTime)

    user = relationship('Users', backref='bookmarks')
    book = relationship('Book', backref='bookmark_users')

class UserLikes(Base):
    __tablename__ = 'user_likes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    timestamp = Column(DateTime)

    user = relationship('Users', backref='likes')
    book = relationship('Book', backref='like_users')

class UserDislikes(Base):
    __tablename__ = 'user_dislikes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    timestamp = Column(DateTime)

    user = relationship('Users', backref='dislikes')
    book = relationship('Book', backref='dislike_users')

class UserRatings(Base):
    __tablename__ = 'user_ratings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    rating = Column(Integer)
    timestamp = Column(DateTime)

    user = relationship('Users', backref='ratings')
    book = relationship('Book', backref='rating_users')

class UserComments(Base):
    __tablename__ = 'user_comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    comment = Column(String)
    timestamp = Column(DateTime)

    user = relationship('Users', backref='comments')
    book = relationship('Book', backref='comment_users')


#create tables and populate them with data
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#populate the tables with data
book1 = Book(title='The Alchemist', author='Paulo Coelho', genre='Adventure')
book2 = Book(title='The Da Vinci Code', author='Dan Brown', genre='Mystery')
book3 = Book(title='The Great Gatsby', author='F. Scott Fitzgerald', genre='Fiction')
book4 = Book(title='The Catcher in the Rye', author='J.D. Salinger', genre='Fiction')

session.add(book1)
session.add(book2)
session.add(book3)
session.add(book4)


session.commit()

# Path: database/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()
