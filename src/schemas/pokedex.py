from pydantic import BaseModel, Field
from typing import Any, List, Optional
from src.utils import PyObjectId
from bson import ObjectId


class PokedexCreate(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    name: str
    age: str
    working_time: str
    proficiency: List[str]
    skills: List[str]
