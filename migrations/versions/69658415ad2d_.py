"""empty message

Revision ID: 69658415ad2d
Revises: 564b3afe668d
Create Date: 2018-10-06 17:02:38.211982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69658415ad2d'
down_revision = '564b3afe668d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('annotation_version', sa.Column('pointer_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_annotation_version_pointer_id'), 'annotation_version', ['pointer_id'], unique=False)
    op.create_foreign_key(None, 'annotation_version', 'annotation', ['pointer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'annotation_version', type_='foreignkey')
    op.drop_index(op.f('ix_annotation_version_pointer_id'), table_name='annotation_version')
    op.drop_column('annotation_version', 'pointer_id')
    # ### end Alembic commands ###