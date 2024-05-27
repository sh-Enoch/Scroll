class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String)
    author_email = Column(String)
    author_book = Column(String)
    author_bio = Column(String)
    nationality =  Column(String)
    relationship('Book', backref='author')
