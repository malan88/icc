"""empty message

Revision ID: 6f6ddcb47ee1
Revises: 69658415ad2d
Create Date: 2018-10-07 08:43:02.021315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f6ddcb47ee1'
down_revision = '69658415ad2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=127), nullable=True),
    sa.Column('author', sa.String(length=127), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('wikipedia', sa.String(length=127), nullable=True),
    sa.Column('gutenberg', sa.String(length=127), nullable=True),
    sa.Column('requester_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('requested', sa.DateTime(), nullable=True),
    sa.Column('approved', sa.DateTime(), nullable=True),
    sa.Column('rejected', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['requester_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_request_approved'), 'book_request', ['approved'], unique=False)
    op.create_index(op.f('ix_book_request_author'), 'book_request', ['author'], unique=False)
    op.create_index(op.f('ix_book_request_book_id'), 'book_request', ['book_id'], unique=False)
    op.create_index(op.f('ix_book_request_rejected'), 'book_request', ['rejected'], unique=False)
    op.create_index(op.f('ix_book_request_requested'), 'book_request', ['requested'], unique=False)
    op.create_index(op.f('ix_book_request_requester_id'), 'book_request', ['requester_id'], unique=False)
    op.create_index(op.f('ix_book_request_title'), 'book_request', ['title'], unique=False)
    op.create_index(op.f('ix_book_request_weight'), 'book_request', ['weight'], unique=False)
    op.create_table('book_request_vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_request_id', sa.Integer(), nullable=True),
    sa.Column('delta', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_request_id'], ['book_request.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_request_vote_book_request_id'), 'book_request_vote', ['book_request_id'], unique=False)
    op.create_index(op.f('ix_book_request_vote_user_id'), 'book_request_vote', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_book_request_vote_user_id'), table_name='book_request_vote')
    op.drop_index(op.f('ix_book_request_vote_book_request_id'), table_name='book_request_vote')
    op.drop_table('book_request_vote')
    op.drop_index(op.f('ix_book_request_weight'), table_name='book_request')
    op.drop_index(op.f('ix_book_request_title'), table_name='book_request')
    op.drop_index(op.f('ix_book_request_requester_id'), table_name='book_request')
    op.drop_index(op.f('ix_book_request_requested'), table_name='book_request')
    op.drop_index(op.f('ix_book_request_rejected'), table_name='book_request')
    op.drop_index(op.f('ix_book_request_book_id'), table_name='book_request')
    op.drop_index(op.f('ix_book_request_author'), table_name='book_request')
    op.drop_index(op.f('ix_book_request_approved'), table_name='book_request')
    op.drop_table('book_request')
    # ### end Alembic commands ###
