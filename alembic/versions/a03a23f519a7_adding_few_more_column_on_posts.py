"""adding few more column on posts

Revision ID: a03a23f519a7
Revises: 9db9d4e93fe5
Create Date: 2022-12-28 21:10:10.621592

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision = 'a03a23f519a7'
down_revision = '9db9d4e93fe5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False,
                                     server_default="TRUE"))
    op.add_column("posts", sa.Column("create_at", sa.TIMESTAMP(timezone=True), nullable=False,
                                     server_default=sa.text("NOW()")))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "create_at")
    pass
