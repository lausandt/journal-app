from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ADD "amount" DECIMAL(10,2);
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" TYPE VARCHAR(25) USING "qualification"::VARCHAR(25);
        ALTER TABLE "fixed_entries" ADD "amount" DECIMAL(10,2);
        ALTER TABLE "fixed_entries" ALTER COLUMN "qualification" TYPE VARCHAR(10) USING "qualification"::VARCHAR(10);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" DROP COLUMN "amount";
        ALTER TABLE "variable_entries" ALTER COLUMN "qualification" TYPE VARCHAR(25) USING "qualification"::VARCHAR(25);
        ALTER TABLE "fixed_entries" DROP COLUMN "amount";
        ALTER TABLE "fixed_entries" ALTER COLUMN "qualification" TYPE VARCHAR(10) USING "qualification"::VARCHAR(10);"""
