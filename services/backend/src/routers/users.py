from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from src.core.dependencies import get_current_user
from src.core.jwthandler import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from src.core.models import User
from src.core.security import validate_user
from src.crud import users
from src.schemas.token import Status
from src.schemas.users import (
    UpdatePassword,
    UserInSchema,
    UserOutSchema,
)

router = APIRouter(
    prefix='/users',
    tags=['Users'],  # dependencies=[Depends(oauth2_scheme)]
)


@router.post('/register', response_model=UserOutSchema)
async def create_user(user: UserInSchema):  # type: ignore
    return await users.create_user(user)


@router.get('/', response_model=list[UserOutSchema])
async def get_users():
    return await users.get_users()


@router.get('/me', response_model=UserOutSchema)
async def get_user_me(current_user: Annotated[User, Depends(get_current_user)]):
    return await users.get_user(id=current_user.id)


@router.get('/user by id/{id}', response_model=UserOutSchema)
async def get_user_by_id(
    id: int, current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.superuser:
        return await users.get_user(id=id)
    raise HTTPException(status_code=403, detail='Not authorized')


@router.patch('/update me', response_model=UserOutSchema)
async def update_user(
    update: UpdatePassword,
    current_user: Annotated[User, Depends(get_current_user)],
):
    return await users.update_user(id=current_user.id, update=update)

@router.patch('/set superuser')
async def set_superuser(id:int ):
    return await users.set_super(id=id)


@router.delete(
    '/remove user/{id}',
    response_model=Status,
)
async def remove_user(
    id: int, current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.superuser or current_user.id == id:
        db_user = await users.get_user(id=id)
        if db_user:
            return await users.delete_user(id)
        raise HTTPException(status_code=404, detail=f'User {id} not found')
    raise HTTPException(status_code=403, detail='Not authorized to delete')


@router.post("/login")
async def login(user: OAuth2PasswordRequestForm = Depends()):
    db_user = await validate_user(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "You've successfully logged in. Welcome back!"}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    )

    return response
