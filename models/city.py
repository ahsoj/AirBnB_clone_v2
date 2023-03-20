#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models import storage_type
from sqlalchemy.orm import relationship
from sqlalchemy import (
Column,
String, 
ForeignKey
)


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_type == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        state_id = ''
        name = ''
