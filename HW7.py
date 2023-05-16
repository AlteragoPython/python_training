from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)

# Create the database
engine = create_engine('sqlite:///films_db.sqlite3')

# Create the table
Base.metadata.create_all(engine)

# Create the table
Base.metadata.create_all(engine)
