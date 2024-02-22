from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" DROP COLUMN "qualification";
        ALTER TABLE "variable_entries" DROP COLUMN "supplier";
        ALTER TABLE "fixed_entries" DROP COLUMN "supplier";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ADD "qualification" VARCHAR(10) NOT NULL  DEFAULT 'Want';
        ALTER TABLE "variable_entries" ADD "supplier" VARCHAR(225) NOT NULL;
        ALTER TABLE "fixed_entries" ADD "supplier" VARCHAR(225) NOT NULL;"""
