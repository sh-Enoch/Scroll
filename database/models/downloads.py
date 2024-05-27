class Downloads(Base):
    __tablename__ = 'downloads'
    download_id = Column(Integer, primary_key=True, autoincrement=True)
    download_content = Column(Integer, ForeignKey('books.id')) #foreign key references book downloaded
    download_user_id = Column(Integer, ForeignKey('users.user_id')) #foreign key references user downloading the book.
    download_date = Column(DateTime)
