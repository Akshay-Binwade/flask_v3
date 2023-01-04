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
