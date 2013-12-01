from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from database.database import Base

class Movie(Base):
    __tablename__ = 'movie'

    movie_id = Column(Integer, primary_key=True)
    title = Column(String)

    def __repr__(self):
        return "<Movie(title='%s')" % (self.title)
