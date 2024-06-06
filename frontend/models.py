from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert, values, LargeBinary
from werkzeug.security import generate_password_hash, check_password_hash
from . import app


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    books = db.relationship('Book', backref='genre', lazy=True)

    def __repr__(self):
        return f"Genre('{self.name}', '{self.description}')"

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    cover_image = db.Column(db.String(150), nullable=True)
    pdf_file = db.Column(db.String(150), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)


    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

""" 
The Post class represents a post in our application. It has four attributes: id, title, content, and date_posted.
The id attribute is the primary key for the table, and it is an auto-incrementing
 integer. The title and content attributes are strings with a maximum length of 100 and 1000 characters, respectively. 
 The date_posted attribute is a DateTime field that stores the date and time when the post was created. 
 The user_id attribute is a foreign key that references the id attribute of the User class.
 The Genre class represents a genre in our application. It has three attributes: id, name, and description.
 The id attribute is the primary key for the table, and it is an auto-incrementing integer.
 The name and description attributes are strings with a maximum length of 100 and 1000 characters, respectively.
 The posts attribute is a relationship to the Post class, which represents the posts in the genre.
 The book class represents a book in our application. It has three attributes: id, title, and author.
 The id attribute is the primary key for the table, and it is an auto-incrementing integer.
 The title and author attributes are strings with a maximum length of 100 characters.
 The genre_id attribute is a foreign key that references the id attribute of the Genre class.
 Each class has a __repr__ method that returns a string representation of the object.
 The User class has two additional methods: set_password and check_password.
 The set_password method takes a password as input, hashes it using the generate_password_hash function from the werkzeug.security module, and stores the hashed password in the password attribute.
 The check_password method takes a password as input, hashes it using the check_password_hash function from the werkzeug.security module, and compares the hashed password with the password attribute.
 If the hashed passwords match, the method returns True; otherwise, it returns False.
 These classes define the structure of the tables in the database and the relationships between them.
 We can use these classes to interact with the database in our Flask application.
 """

book1 = Book(title='Flutter for Beginners', author='Allesandro Biessek', genre_id=1, cover_image='flutter_dart_cookbook.jpg', pdf_file='flutter_and_dart_cookbook.pdf') 
book2 = Book(title='Real-world Svelte', author='Tan Li Hau', genre_id=1, cover_image='realworld.jpg', pdf_file='real_world_svelte.pdf')
book3 = Book(title='Modern Python Web Development', author='Bill Lubanovic', genre_id=1, cover_image='fastapi.jpg', pdf_file='fastapi_modern_python_web_development.pdf')
book4 = Book(title='Mean Stack', author='Pinakin Ashok Chaubal', genre_id=1, cover_image='meanstack.jpg', pdf_file='mastering-mean-stack.pdf')

#add this books under genre_id 2
book6 = Book(title='A Second Chance', author='Sudeep Nagarkar', genre_id=2, cover_image='a_second_chance.jpg', pdf_file='a_second_chance.pdf')
book7 = Book(title='The Scam', author='Sucheta Dalal', genre_id=2, cover_image='the_scam.jpg', pdf_file='the_scam.pdf')
book8 = Book(title='Bared to you', author='Sylivia Day', genre_id=2, cover_image='bared_to_you.jpg', pdf_file='bared_to_you.pdf')


#add this books under genre_id 3
book9 = Book(title='Wings Of Fire', author='A. P. J. Abdul Kalam and Arun Tiwari', genre_id=3, cover_image='wings_of_fire.jpg', pdf_file='wings_of_Fire.pdf')
book10 = Book(title='From Failure to Success', author='Martin Meadows', genre_id=3, cover_image='from_failure_to_Success.jpg', pdf_file='from_failure_to_success.pdf')
book11 = Book(title='The Art of Logical Thinking: Or the Laws of Reasoning', author='William Walker Atkinson',genre_id=3, cover_image= '',pdf_file='the_art_of_Logical_thinking.pdf')


#populate the  genre table genre1= Educational, genre2= Fiction, genre3= Motivational
genre1 = Genre(name='Educational', description='Books that help you learn new skills and knowledge')
genre2 = Genre(name='Fiction', description='Books that tell imaginary stories and events')
genre3 = Genre(name='Motivational', description='Books that inspire and motivate you to achieve your goals')

#commit the changes to the database


