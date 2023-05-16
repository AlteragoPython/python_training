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


# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add 3 films to the film table
film1 = Film(id=1, title="Film1", director="Director1", release_year=2000)
film2 = Film(id=2, title="Film2", director="Director2", release_year=2001)
film3 = Film(id=3, title="Film3", director="Director3", release_year=2002)

session.add(film1)
session.add(film2)
session.add(film3)
session.commit()

# Update 1 film
film_to_update = session.query(Film).filter(Film.id == 1).first()
film_to_update.title = "Updated Film1"
session.commit()

# Print data from table
films = session.query(Film).all()
for film in films:
    print(f'ID: {film.id}, Title: {film.title}, Director: {film.director}, Release Year: {film.release_year}')

# Delete all data from table
session.query(Film).delete()
session.commit()
