from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "full_name" VARCHAR(50) NOT NULL,
    "password" VARCHAR(128) NOT NULL,
    "active" BOOL   DEFAULT True,
    "superuser" BOOL   DEFAULT False,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "variable_entries" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(225) NOT NULL,
    "amount" DECIMAL(10,2),
    "supplier" VARCHAR(225),
    "qualification" VARCHAR(25) NOT NULL  DEFAULT 'Want',
    "note" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "author_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "variable_entries"."qualification" IS 'Need: Need\nWant: Want\nLeisure: Leisure\nUnexpected: Unexpected';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
