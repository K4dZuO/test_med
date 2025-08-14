from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import User
from app.db import get_session


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, user_id: int):
        result = self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
    
    
def get_user_service(session: Session = Depends(get_session)):
    return UserService(session)
