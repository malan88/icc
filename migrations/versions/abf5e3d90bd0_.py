"""empty message

Revision ID: abf5e3d90bd0
Revises: 7aa76548d98e
Create Date: 2018-07-12 13:45:02.653798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abf5e3d90bd0'
down_revision = '7aa76548d98e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('url', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'url')
    # ### end Alembic commands ###