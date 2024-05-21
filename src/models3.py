import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favorite_people = Table(
    "favorite_people",
    Base.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('people_id', ForeignKey('people.id'), primary_key=True)
)

favorite_starships = Table(
    "favorite_starships",
    Base.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('starship_id', ForeignKey('starships.id'), primary_key=True)
)

favorite_planets = Table(
    "favorite_planets",
    Base.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('planet_id', ForeignKey('planets.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    last_name = Column(String(32))
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(32), nullable=False)
    people_relationship = relationship("People", secondary=favorite_people, back_populates="user")
    starships_relationship = relationship("Starships", secondary=favorite_starships, back_populates="user")

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
    user_relationship = relationship("User", secondary=favorite_people, back_populates="people")

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    model = Column(String(50))
    starship_class = Column(String(50))
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    user_relationship = relationship("User", secondary=favorite_starships, back_populates="starships")

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
    user_relationship = relationship("User", secondary=favorite_planets, back_populates="planets")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
