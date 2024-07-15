from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
import enum

Base = declarative_base()

class Role(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class UserType(enum.Enum):
    BUYER = "buyer"
    SELLER = "seller"

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(Role), nullable=False)
    user_type = Column(Enum(UserType))