from pydantic import BaseModel


class Machine(BaseModel):
    name: str
    version: str
    auteur: str
    licence: str

