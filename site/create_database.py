from database.database import engine, Base
from model.movie import Movie


Base.metadata.create_all(engine)
