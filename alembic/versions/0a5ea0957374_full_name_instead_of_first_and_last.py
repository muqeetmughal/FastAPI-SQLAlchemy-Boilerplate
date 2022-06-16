"""full name instead of first and last

Revision ID: 0a5ea0957374
Revises: 994aa459c80a
Create Date: 2022-06-14 19:41:14.841637

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0a5ea0957374'
down_revision = '994aa459c80a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.String(length=75), nullable=True))
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', mysql.VARCHAR(length=30), nullable=True))
    op.add_column('users', sa.Column('last_name', mysql.VARCHAR(length=30), nullable=True))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###
