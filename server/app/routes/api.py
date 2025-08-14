from fastapi import APIRouter, Depends, HTTPException

from app.models import UserResponse
from app.services.user_service import UserService, get_user_service

router = APIRouter(prefix='/auth',
                   tags=['auth'])


@router.get('/test', response_model=UserResponse)
async def test():
    return UserResponse(id=0,
                        username="Nick",
                        age=12)


@router.get('/users/{id}', response_model=UserResponse)
async def read_user(id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user_by_id(id)
    if not user: 
        raise HTTPException(status_code=404, detail="User not found")
    return user
