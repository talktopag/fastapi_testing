"""Add extra columns to posts Table

Revision ID: 7a6ef0069dd1
Revises: 2671d8888e82
Create Date: 2023-05-24 10:54:39.639629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a6ef0069dd1'
down_revision = '2671d8888e82'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
