"""empty message

Revision ID: 7aa76548d98e
Revises: 
Create Date: 2018-07-11 14:32:15.259083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7aa76548d98e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('death_date', sa.Date(), nullable=True),
    sa.Column('ts_added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_author_birth_date'), 'author', ['birth_date'], unique=False)
    op.create_index(op.f('ix_author_death_date'), 'author', ['death_date'], unique=False)
    op.create_index(op.f('ix_author_first_name'), 'author', ['first_name'], unique=False)
    op.create_index(op.f('ix_author_last_name'), 'author', ['last_name'], unique=False)
    op.create_index(op.f('ix_author_name'), 'author', ['name'], unique=False)
    op.create_index(op.f('ix_author_ts_added'), 'author', ['ts_added'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.VARCHAR(length=128, collation='utf8mb4_bin'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_word_word'), 'word', ['word'], unique=True)
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('published', sa.Date(), nullable=True),
    sa.Column('ts_added', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_author_id'), 'book', ['author_id'], unique=False)
    op.create_table('position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('word_id', sa.Integer(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['word_id'], ['word.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_position_book_id'), 'position', ['book_id'], unique=False)
    op.create_index(op.f('ix_position_number'), 'position', ['number'], unique=False)
    op.create_index(op.f('ix_position_position'), 'position', ['position'], unique=False)
    op.create_index(op.f('ix_position_word_id'), 'position', ['word_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_position_word_id'), table_name='position')
    op.drop_index(op.f('ix_position_position'), table_name='position')
    op.drop_index(op.f('ix_position_number'), table_name='position')
    op.drop_index(op.f('ix_position_book_id'), table_name='position')
    op.drop_table('position')
    op.drop_index(op.f('ix_book_author_id'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_word_word'), table_name='word')
    op.drop_table('word')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_author_ts_added'), table_name='author')
    op.drop_index(op.f('ix_author_name'), table_name='author')
    op.drop_index(op.f('ix_author_last_name'), table_name='author')
    op.drop_index(op.f('ix_author_first_name'), table_name='author')
    op.drop_index(op.f('ix_author_death_date'), table_name='author')
    op.drop_index(op.f('ix_author_birth_date'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###