"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List, Optional
from models.basemodel import Base
from pydantic import BaseModel


class Vehicles_from_db(BaseModel):
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: Optional[str]
    vehicle_class: str
    created: str
    edited: str
    url: str

class V_PostOrPut(Base):
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: int
    vehicle_class: str

class Vehicle_(Base):
    """ Pydantic model class meant to validate the data for `Vehicle` object from
        single resource endpoint from starwars API.
    """

    # attribute fields
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    crew: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: int
    vehicle_class: str

    # relationship attribute fields
    pilots: Optional[List[str]]
    films: Optional[List[str]]

if __name__ == '__main__':
    data ={
    "name": "Sand Crawler",
    "model": "Digger Crawler",
    "manufacturer": "Corellia Mining Corporation",
    "cost_in_credits": "150000",
    "length": "36.8 ",
    "max_atmosphering_speed": "30",
    "crew": "46",
    "passengers": "30",
    "cargo_capacity": "50000",
    "consumables": "2 months",
    "vehicle_class": "wheeled",
    "pilots": [],
    "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/5/"
    ],
    "created": "2014-12-10T15:36:25.724000Z",
    "edited": "2014-12-20T21:30:21.661000Z",
    "url": "https://swapi.dev/api/vehicles/4/"}

    valid = V_PostOrPut(**data)
    print(valid)