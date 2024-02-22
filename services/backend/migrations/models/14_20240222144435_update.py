from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ALTER COLUMN "created_at" SET NOT NULL;
        ALTER TABLE "variable_entries" ALTER COLUMN "created_at" TYPE DATE USING "created_at"::DATE;
        ALTER TABLE "fixed_entries" ALTER COLUMN "created_at" SET NOT NULL;
        ALTER TABLE "fixed_entries" ALTER COLUMN "created_at" TYPE DATE USING "created_at"::DATE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        ALTER TABLE "variable_entries" ALTER COLUMN "created_at" DROP NOT NULL;
        ALTER TABLE "fixed_entries" ALTER COLUMN "created_at" TYPE TIMESTAMPTZ USING "created_at"::TIMESTAMPTZ;
        ALTER TABLE "fixed_entries" ALTER COLUMN "created_at" DROP NOT NULL;"""
