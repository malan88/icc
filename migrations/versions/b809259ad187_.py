"""empty message

Revision ID: b809259ad187
Revises: 0a91abb0bd0a
Create Date: 2018-07-21 09:06:18.201973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b809259ad187'
down_revision = '0a91abb0bd0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('break', sa.Column('break_title', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('break', 'break_title')
    # ### end Alembic commands ###
