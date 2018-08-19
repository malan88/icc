"""empty message

Revision ID: eb799e906153
Revises: 4d8a274b3563
Create Date: 2018-08-19 10:43:16.953596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb799e906153'
down_revision = '4d8a274b3563'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('line', sa.Column('em_status_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_line_em_status_id'), 'line', ['em_status_id'], unique=False)
    op.create_foreign_key(None, 'line', 'kind', ['em_status_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'line', type_='foreignkey')
    op.drop_index(op.f('ix_line_em_status_id'), table_name='line')
    op.drop_column('line', 'em_status_id')
    # ### end Alembic commands ###
