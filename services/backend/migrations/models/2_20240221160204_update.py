from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" DROP COLUMN "amount";
        ALTER TABLE "fixed_entries" DROP COLUMN "amount";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ADD "amount" DECIMAL(10,2) NOT NULL;
        ALTER TABLE "fixed_entries" ADD "amount" DECIMAL(10,2) NOT NULL;"""
