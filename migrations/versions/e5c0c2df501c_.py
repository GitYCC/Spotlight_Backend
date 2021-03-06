"""empty message

Revision ID: e5c0c2df501c
Revises: 0d44ca3482fa
Create Date: 2019-03-26 17:20:31.575446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5c0c2df501c'
down_revision = '0d44ca3482fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Spots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('zone', sa.String(length=20), nullable=False),
    sa.Column('describe', sa.String(length=5000), nullable=True),
    sa.Column('tel', sa.String(length=255), nullable=True),
    sa.Column('website', sa.String(length=500), nullable=True),
    sa.Column('keyword', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=500), nullable=True),
    sa.Column('pic1', sa.String(length=500), nullable=True),
    sa.Column('pic2', sa.String(length=500), nullable=True),
    sa.Column('pic3', sa.String(length=500), nullable=True),
    sa.Column('px', sa.Float(precision=18), nullable=True),
    sa.Column('py', sa.Float(precision=18), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Spots')
    # ### end Alembic commands ###
