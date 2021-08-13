"""create users table

Revision ID: 4779b78a998c
Revises:
Create Date: 2021-05-07 18:14:16.174907

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4779b78a998c"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.CHAR(32), primary_key=True),
        sa.Column("first_name", sa.String(50), nullable=False),
        sa.Column("last_name", sa.String(80), nullable=False),
        sa.Column("email", sa.String(50), nullable=False),
        sa.Column("password", sa.String(120)),
        sa.Column("updated_at", sa.DateTime),
        sa.Column("created_at", sa.DateTime),
    )


def downgrade():
    op.drop_table("users")
