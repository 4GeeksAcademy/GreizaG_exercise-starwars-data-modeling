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
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(32), nullable=False)
    user_favorite_people = relationship("FavoritePeople", back_populates="user_id_relationship")
    user_favorite_planets = relationship("FavoritePlanets", back_populates="user_id_relationship")
    user_favorite_starships = relationship("FavoriteStarships", back_populates="user_id_relationship")

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    heigth = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(20))
    eye_color = Column(String(20))
    skin_color = Column(String(20))
    birth_year = Column(String(20))
    gender = Column(String(20))
    favorite_people = relationship("FavoritePeople", back_populates="people_id_relationship")

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    model = Column(String(50))
    starship_class = Column(String(50))
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    favorite_starships = relationship("FavoriteStarships", back_populates="starships_id_relationship")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    diameter = Column(Integer)
    gravity = Column(String(50))
    population = Column(Integer)
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(Integer)
    favorite_planets = relationship("FavoritePlanets", back_populates="planets_id_relationship")

class FavoritePeople(Base):
    __tablename__ = 'favorite_people'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship("User", back_populates="user_favorite_people")
    people_id = Column(Integer, ForeignKey('people.id'))
    people_id_relationship = relationship("People", back_populates="favorite_people")

class FavoriteStarships(Base):
    __tablename__ = 'favorite_starships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship("User", back_populates="user_favorite_starships")
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships_id_relationship = relationship("Starships", back_populates="favorite_starships")

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship("User", back_populates="user_favorite_planets")
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets_id_relationship = relationship("Planets", back_populates="favorite_planets")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
