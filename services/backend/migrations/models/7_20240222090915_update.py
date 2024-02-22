from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ADD "qualification" VARCHAR(10)   DEFAULT 'Want';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" DROP COLUMN "qualification";"""
