from pydantic import BaseModel
from datetime import datetime
from typing import Union

class Candidates(BaseModel):
    candidate_id: int
    name: str
    vision: Union[str, None] = None
    mission: Union[str, None] = None

class Votes(BaseModel):
    candidate_id: int

