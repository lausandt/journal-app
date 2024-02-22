from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ADD "created_at" DATE;
        ALTER TABLE "fixed_entries" ADD "created_at" DATE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" DROP COLUMN "created_at";
        ALTER TABLE "fixed_entries" DROP COLUMN "created_at";"""
