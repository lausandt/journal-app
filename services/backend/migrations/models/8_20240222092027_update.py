from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" DROP DEFAULT;
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" TYPE VARCHAR(20) USING "qualification"::VARCHAR(20);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" SET DEFAULT 'Want';
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" TYPE VARCHAR(10) USING "qualification"::VARCHAR(10);"""
