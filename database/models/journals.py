class Journals(Base):
    __tablename = 'journals'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    editor = Column(String)
    topic = Column(String)

    __tablename = 'journals'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    editor = Column(String)
    topic = Column(String)
