import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    last_name = Column(String(32))
    email = Column(String(50), nullable=False)
    password = Column(Sting(32), nullable=False)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    heigth = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    eye_color = Column(String)
    skin_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    starship_class = Column(String)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    diameter = Column(Integer)
    gravity = Column(String)
    population = Column(Integer)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(Integer)

class FavoritePeople(Base):
    __tablename__ = 'favorite_people'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    people_id = Column(Integer, ForeignKey('people.id'))
    people_id_relationship = relationship(People)

class FavoriteStarships(Base):
    __tablename__ = 'favorite_starships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships_id_relationship = relationship(Starships)

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets_id_relationship = relationship(Planets)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
