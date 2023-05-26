"""Create posts Table

Revision ID: 2671d8888e82
Revises: 
Create Date: 2023-05-24 10:47:04.653165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2671d8888e82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", 
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table('posts')
