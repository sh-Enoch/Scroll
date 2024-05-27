from db import *

class UserBooks(Base):
    __tablename__ = 'user_books'
    user_book_id = Column(Integer,primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id')) #foreign key references book 
    read_status = Column(String)
    read_timestamp = Column(DateTime)
