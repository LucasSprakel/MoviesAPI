from typing import Optional

from pydantic import BaseModel as SCBaseModel



class MovieSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    nota: int
    sinopse: str

    class Config:
        orm_mode = True