"""adding new column content

Revision ID: 9dac1ff27239
Revises: 2699215ab612
Create Date: 2022-12-28 18:22:57.900855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dac1ff27239'
down_revision = '2699215ab612'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
