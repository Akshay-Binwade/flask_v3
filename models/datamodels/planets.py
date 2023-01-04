"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List, Optional
from decimal import Decimal
from models.basemodel import Base
from pydantic import BaseModel, validator

class Plan_from_db(BaseModel):
    climate: str
    diameter: str
    gravity: str
    name: str
    orbital_period: str
    population: str
    rotation_period: str
    surface_water: str
    terrain: str
    created: str
    edited: str
    url: str

class P_PostOrPut(Base):
    climate: str
    diameter: str
    gravity: str
    name: str
    orbital_period: str
    population: str
    rotation_period: str
    surface_water: str
    terrain: str

    @validator("population")
    @classmethod
    def val_people(cls, population):
        try:
            population == int(population)
        except ValueError:
            return 0
        return population

class P_Patch(BaseModel):
    climate: Optional[str]
    diameter: Optional[str]
    gravity: Optional[str]
    name: Optional[str]
    orbital_period: Optional[str]
    population: Optional[str]
    rotation_period: Optional[str]
    surface_water: Optional[str]
    terrain: Optional[str]
    created: Optional[str]
    edited: Optional[str]
    url: Optional[str]

class Planet_(Base):
    """ Pydantic model class meant to validate the data for `Planet` object from
        single resource endpoint from starwars API.
    """

    # attribute fields
    climate: str
    diameter: str
    gravity: str
    name: str
    orbital_period: str
    population: str
    rotation_period: str
    surface_water: str
    terrain: str

    # Relationship attribute fields
    films: Optional[List[str]]
    residents: Optional[List[str]]
