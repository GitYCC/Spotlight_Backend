"""empty message

Revision ID: 3859b41d96b5
Revises: 3ab61dfbd0ca
Create Date: 2019-03-30 22:58:06.115807

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3859b41d96b5'
down_revision = '3ab61dfbd0ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('FavoriteSpots', 'update_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('FavoriteSpots', sa.Column('update_time', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
