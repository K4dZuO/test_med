from fastapi import APIRouter
from pydantic import BaseModel


class UserResponse(BaseModel):
    name: str
    age: int

router = APIRouter(prefix='/auth',
                   tags=['auth'])


@router.get('/logs', response_model=UserResponse)
async def logs():
    return {'name': "Nick",
            'age': 44}
