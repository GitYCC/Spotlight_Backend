"""empty message

Revision ID: bb15eb874521
Revises: e5c0c2df501c
Create Date: 2019-03-28 22:21:54.586029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb15eb874521'
down_revision = 'e5c0c2df501c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Projects',
    sa.Column('proj_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=False),
    sa.Column('start_day', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('end_day', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('plan', sa.String(length=5000), nullable=False),
    sa.Column('created_time', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('update_time', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('proj_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Projects')
    # ### end Alembic commands ###
