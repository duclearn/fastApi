"""add user_id foreign key with users id

Revision ID: 9db9d4e93fe5
Revises: ff32f4b2fc48
Create Date: 2022-12-28 20:26:32.552196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9db9d4e93fe5'
down_revision = 'ff32f4b2fc48'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_userid_fk", source_table="posts", referent_table="users",
                          local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint(constraint_name="posts_userid_fk", table_name="posts")
    op.drop_column(table_name="posts", column_name="owner_id")
    pass
