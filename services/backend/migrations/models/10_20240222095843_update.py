from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" SET DEFAULT 'Want';
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" TYPE VARCHAR(25) USING "qualification"::VARCHAR(25);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" TYPE VARCHAR(25) USING "qualification"::VARCHAR(25);
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" DROP DEFAULT;"""
