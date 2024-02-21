from typing import Annotated

from fastapi import Depends
from jose import JWTError, jwt

from src.schemas.token import TokenData
from src.schemas.users import UserDatabaseSchema

from .jwthandler import ALGORITHM, SECRET_KEY, credentials_exception, security
from .models import User


async def get_current_user(
    token: Annotated[str, Depends(security)],
) -> UserDatabaseSchema:  # type: ignore
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await UserDatabaseSchema.from_queryset_single(
        User.get(username=token_data.username)
    )
    if user is None:
        raise credentials_exception
    return user
