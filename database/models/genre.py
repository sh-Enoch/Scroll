class Genre(Base):
    __tablename__ = 'genre'
    genre_id = Column(Integer, primary_key=True, autoincrement=True)
    genre_name = Column(String)
    genre_books = Column(Integer, ForeignKey('books.id')) #foreign key  references book_id

