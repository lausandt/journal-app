from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" SET NOT NULL;
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" TYPE VARCHAR(25) USING "qualification"::VARCHAR(25);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" TYPE VARCHAR(20) USING "qualification"::VARCHAR(20);
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" DROP NOT NULL;"""
