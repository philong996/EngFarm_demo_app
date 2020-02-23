from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///EngFarm.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __repr__(self):
        return "{}".format(self.name)

class Lesson(Base):
    """"""
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(String)
    creator = Column(String)
    media_type = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("user", backref=backref(
        "lesson", order_by=id))


# create tables
Base.metadata.create_all(engine)