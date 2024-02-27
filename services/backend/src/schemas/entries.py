"""
1 - EntryInSchema create new entries
2 - EntryOutSchema entry object for use outside of the application
3 - UpdateEntry schemas for updating existing entries
"""
from decimal import Decimal

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.core.models import Entry # FixedEntry, Interval

EntryInSchema = pydantic_model_creator(
    Entry, name="EntryIn", exclude=["author_id"], exclude_readonly=True)

EntryOutSchema = pydantic_model_creator(
    Entry, name="EntryOut",
    exclude=[
        "author.password",
        "author.superuser",
        "author.active",
        "author.budget",
        "author.username",
        "author.regular_entry",
        "author.savings_goal",
        'author.fixeds',
    ],
)

# FixedEntryInSchema = pydantic_model_creator(
#     FixedEntry, name="FixedEntryIn", exclude=["author_id"], exclude_readonly=True
# )

# FixedEntryOutSchema = pydantic_model_creator(
#     FixedEntry,
#     name="FixedEntryOut",
#     exclude=[
#         "author.password",
#         "author.superuser",
#         "author.entry",
#         "author.active",
#         "author.budget",
#         "author.username",
#         "author.savings_goal",
#     ],
# )


class UpdateEntry(BaseModel):
    title: str | None
    note: str | None
    amount: Decimal | None


# class UpdateFixedEntry(BaseModel):
#     title: str | None
#     content: str | None
#     amount: Decimal | None
#     interval: Interval | None