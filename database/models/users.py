from db import *

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement= True)
    user_name = Column(String)
    user_email = Column(String)
    user_password =  Column(unique=True)
