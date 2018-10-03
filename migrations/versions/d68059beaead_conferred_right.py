"""conferred_right

Revision ID: d68059beaead
Revises: 2ef8c08f29ba
Create Date: 2018-10-03 10:13:18.815977

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd68059beaead'
down_revision = '2ef8c08f29ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conferred_rights',
    sa.Column('right_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['right_id'], ['admin_right.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.drop_table('rights')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rights',
    sa.Column('right_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['right_id'], ['admin_right.id'], name='rights_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='rights_ibfk_2'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('conferred_rights')
    # ### end Alembic commands ###
