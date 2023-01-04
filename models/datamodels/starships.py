"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List, Optional
from decimal import Decimal
from models.basemodel import Base
from pydantic import BaseModel


class Starships_from_db(BaseModel):
    MGLT: str
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: str
    hyperdrive_rating: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    starship_class: str
    passengers: str
    created: str
    edited: str
    url: str


class St_PutOrPost(Base):
    MGLT: str
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: str
    hyperdrive_rating: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    starship_class: str
    passengers: str

class St_Patch(BaseModel):
    MGLT: Optional[str]
    cargo_capacity: Optional[str]
    consumables: Optional[str]
    cost_in_credits: Optional[str]
    crew: Optional[str]
    hyperdrive_rating: Optional[str]
    length: Optional[str]
    manufacturer: Optional[str]
    max_atmosphering_speed: Optional[str]
    model: Optional[str]
    name: Optional[str]
    starship_class: Optional[str]
    passengers: Optional[str]
    created: Optional[str]
    edited: Optional[str]
    url: Optional[str]

class Starship_(Base):
    """ Pydantic model class meant to validate the data for `Starship` object from single resource
        endpoint from starwars API.
    """

    # attribute fields
    MGLT: str
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: str
    hyperdrive_rating: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    starship_class: str
    passengers: str

    # relationship attribute fields
    films: Optional[List[str]]
    pilots: Optional[List[str]]
