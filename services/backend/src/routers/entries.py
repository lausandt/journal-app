from enum import Enum
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependencies import get_current_user
from src.core.models import User
from src.crud import entries
from src.schemas.entries import (
    EntryInSchema,
    EntryOutSchema,
    # FixedEntryInSchema,
    # FixedEntryOutSchema,
    # UpdateEntry,
    # UpdateFixedEntry,
)
from src.schemas.token import Status

router = APIRouter(
    prefix="/entries",
    tags=["Entries"],  # dependencies=[Depends(oauth2_scheme)]
)

@router.post("/create entry", response_model=EntryOutSchema)
async def create_entry(
    entry: EntryInSchema, current_user: Annotated[User, Depends(get_current_user)] # type: ignore
): 
    return await entries.create_entry(entry=entry, user_id=current_user.id)

@router.get("/my entries", response_model=list[EntryOutSchema])
async def get_my_entries(current_user: Annotated[User, Depends(get_current_user)]):  
    return await entries.get_my_entries(current_user.id)

@router.delete("/delete entry", response_model=Status)
async def remove_entry(id:int, current_user: Annotated[User, Depends(get_current_user)]):
    return await entries.remove_entry(id=id, user=current_user)

