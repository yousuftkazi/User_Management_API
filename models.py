from enum import Enum
import pydantic
from pydantic import BaseModel

class TVShow(str, Enum):
    breaking_bad = "breaking_bad"
    the_wire = "the_wire"

class User(BaseModel):
    id: int
    name: str
    favorite_tv_show: TVShow