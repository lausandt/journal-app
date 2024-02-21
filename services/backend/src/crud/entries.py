from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.core.models import Entry, FixedEntry, User
from src.schemas.entries import (
    EntryInSchema,
    EntryOutSchema,
    # FixedEntryInSchema,
    # FixedEntryOutSchema,
    # UpdateEntry,
    # UpdateFixedEntry,
)
from src.schemas.token import Status


async def create_entry(entry: EntryInSchema, user_id: int) -> EntryOutSchema: # type: ignore
    entry_dict = entry.dict(exclude_unset=True)
    entry_dict["author_id"] = user_id
    entry_obj = await Entry.create(**entry_dict)
    return await EntryOutSchema.from_tortoise_orm(entry_obj)

async def get_my_entries(user_id) -> list[EntryOutSchema]: # type: ignore
    entries = await EntryOutSchema.from_queryset(Entry.all())
    return [e for e in entries if e.author.id == user_id]

async def remove_entry(id: int, user:User) -> Status:
    try:
        entry = await EntryOutSchema.from_queryset_single(Entry.get(id=id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f'there is no entry with id {id}')

    if user.id == entry.author.id or user.superuser:
        await Entry.filter(id=id).delete()
        return Status(message=f'Deleted entry with ID: {id}')
    raise HTTPException(status_code=403, detail='User is not permitted to perform this action')
