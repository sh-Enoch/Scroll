class Reviews(Base):
    __tablename__ = 'Reviews'
    review_id = Column(Integer, autoincrement=True)
    review_user_id = Column(Integer, ForeignKey('users.user_id')) #foreign key references the user_id from users
    rating = Column(Integer)
    comment = Column(String)
