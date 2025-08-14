from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy import String, Integer

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)

    
class UserResponse(BaseModel):
    id: int
    username: str
    age: int
