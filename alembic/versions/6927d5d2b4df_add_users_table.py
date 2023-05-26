"""Add users table

Revision ID: 6927d5d2b4df
Revises: 7a6ef0069dd1
Create Date: 2023-05-24 10:58:56.819357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6927d5d2b4df'
down_revision = '7a6ef0069dd1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", 
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String, nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))


def downgrade() -> None:
    op.drop_table("users")
