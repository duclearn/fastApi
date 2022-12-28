"""empty message

Revision ID: 2699215ab612
Revises: 
Create Date: 2022-12-28 18:17:31.246905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2699215ab612'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("items", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
