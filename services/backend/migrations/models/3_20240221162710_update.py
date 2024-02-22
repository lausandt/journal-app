from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" DROP COLUMN "modified_at";
        ALTER TABLE "variable_entries" DROP COLUMN "created_at";
        ALTER TABLE "fixed_entries" DROP COLUMN "modified_at";
        ALTER TABLE "fixed_entries" DROP COLUMN "created_at";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ADD "modified_at" DATE NOT NULL;
        ALTER TABLE "variable_entries" ADD "created_at" DATE NOT NULL;
        ALTER TABLE "fixed_entries" ADD "modified_at" DATE NOT NULL;
        ALTER TABLE "fixed_entries" ADD "created_at" DATE NOT NULL;"""
