from pydantic import BaseModel


class User(BaseModel):
    id: int
    public_id = str
    name: str
    password = str
    admin = bool

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    name:str
    password: str

    class Config:
        orm_mode = True