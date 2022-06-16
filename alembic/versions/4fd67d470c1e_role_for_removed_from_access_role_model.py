"""role_for removed from access.Role Model

Revision ID: 4fd67d470c1e
Revises: 0a5ea0957374
Create Date: 2022-06-16 21:18:56.117511

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4fd67d470c1e'
down_revision = '0a5ea0957374'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'role_for')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('role_for', mysql.VARCHAR(length=50), nullable=False))
    # ### end Alembic commands ###
