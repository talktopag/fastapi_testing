"""add additional columns to posts

Revision ID: 1565d1c31e66
Revises: 97c42786a6b3
Create Date: 2023-05-24 11:10:11.646960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1565d1c31e66'
down_revision = '97c42786a6b3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))


def downgrade() -> None:
    op.drop_column("posts", column_name='published')
    op.drop_column("posts", column_name='created_at')
