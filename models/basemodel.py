"""
This module defines a pydantic basemodel to be used by another
pydantic models (resource models aka "datamodels")
"""

from pydantic import BaseModel,validator
from datetime import datetime,date
from typing import Union, Optional

class Base(BaseModel):
    """common attributes available in all resources"""

    created: datetime
    edited: datetime
    url: str

    @validator("created")
    @classmethod
    def created_on(cls,created):
        if isinstance(created, datetime) or isinstance(created,date):
            return created.strftime("%Y-%m-%d")

    @validator("edited")
    @classmethod
    def edited_on(cls,edited):
        if isinstance(edited,datetime) or isinstance(edited,date):
            return edited.strftime("%Y-%m-%d")


if __name__ == "__main__":
    data = {
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://swapi.dev/api/people/1/"
    }

    # breakpoint()

    obj = Base(**data)
    print(obj.created)
    print(type(obj.created))
    print("****" * 10)
    print(obj)
