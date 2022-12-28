"""create users table

Revision ID: ff32f4b2fc48
Revises: 9dac1ff27239
Create Date: 2022-12-28 18:31:46.802032

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text

# revision identifiers, used by Alembic.
revision = 'ff32f4b2fc48'
down_revision = '9dac1ff27239'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("create_at", sa.TIMESTAMP(timezone=True),
                              server_default=text("NOW()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email"))
    pass


def downgrade():
    op.drop_table("users")
    pass
