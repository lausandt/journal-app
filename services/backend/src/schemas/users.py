"""
Tortoise comes with a pydantic model creating function
which creates the pydantic models for you:
1 - User/SuperInSchema for creating new users
2 - User/SuperOutSchema, user objects for use outside the application
3 - User/SuperDatabaseSchema, user object for use within the application for most for validation
4 - UpdatePassword to update a user's password
"""
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.core.models import User

UserInSchema = pydantic_model_creator(
    User,
    name='UserIn',
    exclude=['created_at', 'active'],
    exclude_readonly=True
    
)


UserOutSchema = pydantic_model_creator(
    User,
    name='User',
    exclude=['active', 'entries','fixeds', 'savings_goal', 'superuser'],
)

UserDatabaseSchema = pydantic_model_creator(User, name='User')


class UpdatePassword(BaseModel):
    password: str | None

