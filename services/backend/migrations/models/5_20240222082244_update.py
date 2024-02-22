from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ADD "amount" DECIMAL(10,2);
        ALTER TABLE "variable_entries" ADD "supplier" VARCHAR(225);
        ALTER TABLE "variable_entries" ADD "qualification" VARCHAR(10)   DEFAULT 'Want';
        ALTER TABLE "variable_entries" DROP COLUMN "created_at";
        ALTER TABLE "variable_entries" DROP COLUMN "modified_at";
        ALTER TABLE "fixed_entries" ADD "amount" DECIMAL(10,2);
        ALTER TABLE "fixed_entries" ADD "supplier" VARCHAR(225);
        ALTER TABLE "fixed_entries" DROP COLUMN "created_at";
        ALTER TABLE "fixed_entries" DROP COLUMN "modified_at";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "variable_entries" ADD "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "variable_entries" ADD "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "variable_entries" DROP COLUMN "amount";
        ALTER TABLE "variable_entries" DROP COLUMN "supplier";
        ALTER TABLE "variable_entries" DROP COLUMN "qualification";
        ALTER TABLE "fixed_entries" ADD "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "fixed_entries" ADD "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "fixed_entries" DROP COLUMN "amount";
        ALTER TABLE "fixed_entries" DROP COLUMN "supplier";"""
