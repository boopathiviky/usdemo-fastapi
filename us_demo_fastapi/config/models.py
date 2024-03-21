from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from .db import Base


class User(Base):

    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    public_id = Column(String(50), unique=True)
    name = Column(String(50))
    password = Column(String(80))
    admin = Column(Boolean)