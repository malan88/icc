"""empty message

Revision ID: cc25bf90e82e
Revises: 
Create Date: 2018-08-30 15:09:42.506944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc25bf90e82e'
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
    sa.Column('url', sa.String(length=128), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('death_date', sa.Date(), nullable=True),
    sa.Column('added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_author_added'), 'author', ['added'], unique=False)
    op.create_index(op.f('ix_author_birth_date'), 'author', ['birth_date'], unique=False)
    op.create_index(op.f('ix_author_death_date'), 'author', ['death_date'], unique=False)
    op.create_index(op.f('ix_author_first_name'), 'author', ['first_name'], unique=False)
    op.create_index(op.f('ix_author_last_name'), 'author', ['last_name'], unique=False)
    op.create_index(op.f('ix_author_name'), 'author', ['name'], unique=False)
    op.create_index(op.f('ix_author_url'), 'author', ['url'], unique=False)
    op.create_table('kind',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kind', sa.String(length=12), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_kind_kind'), 'kind', ['kind'], unique=False)
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tag_tag'), 'tag', ['tag'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('sort_title', sa.String(length=128), nullable=True),
    sa.Column('url', sa.String(length=128), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('summary', sa.Text(), nullable=True),
    sa.Column('published', sa.Date(), nullable=True),
    sa.Column('added', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_author_id'), 'book', ['author_id'], unique=False)
    op.create_index(op.f('ix_book_sort_title'), 'book', ['sort_title'], unique=False)
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=False)
    op.create_index(op.f('ix_book_url'), 'book', ['url'], unique=False)
    op.create_table('annotation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('added', sa.DateTime(), nullable=True),
    sa.Column('edit_pending', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_annotation_added'), 'annotation', ['added'], unique=False)
    op.create_index(op.f('ix_annotation_author_id'), 'annotation', ['author_id'], unique=False)
    op.create_index(op.f('ix_annotation_book_id'), 'annotation', ['book_id'], unique=False)
    op.create_index(op.f('ix_annotation_edit_pending'), 'annotation', ['edit_pending'], unique=False)
    op.create_table('line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('l_num', sa.Integer(), nullable=True),
    sa.Column('kind_id', sa.Integer(), nullable=True),
    sa.Column('bk_num', sa.Integer(), nullable=True),
    sa.Column('pt_num', sa.Integer(), nullable=True),
    sa.Column('ch_num', sa.Integer(), nullable=True),
    sa.Column('em_status_id', sa.Integer(), nullable=True),
    sa.Column('line', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['em_status_id'], ['kind.id'], ),
    sa.ForeignKeyConstraint(['kind_id'], ['kind.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_line_bk_num'), 'line', ['bk_num'], unique=False)
    op.create_index(op.f('ix_line_book_id'), 'line', ['book_id'], unique=False)
    op.create_index(op.f('ix_line_ch_num'), 'line', ['ch_num'], unique=False)
    op.create_index(op.f('ix_line_em_status_id'), 'line', ['em_status_id'], unique=False)
    op.create_index(op.f('ix_line_kind_id'), 'line', ['kind_id'], unique=False)
    op.create_index(op.f('ix_line_l_num'), 'line', ['l_num'], unique=False)
    op.create_index(op.f('ix_line_pt_num'), 'line', ['pt_num'], unique=False)
    op.create_table('annotation_version',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('editor_id', sa.Integer(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('pointer_id', sa.Integer(), nullable=True),
    sa.Column('hash_id', sa.String(length=40), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('previous_id', sa.Integer(), nullable=True),
    sa.Column('first_line_num', sa.Integer(), nullable=True),
    sa.Column('last_line_num', sa.Integer(), nullable=True),
    sa.Column('first_char_idx', sa.Integer(), nullable=True),
    sa.Column('last_char_idx', sa.Integer(), nullable=True),
    sa.Column('annotation', sa.Text(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('tag_1_id', sa.Integer(), nullable=True),
    sa.Column('tag_2_id', sa.Integer(), nullable=True),
    sa.Column('tag_3_id', sa.Integer(), nullable=True),
    sa.Column('tag_4_id', sa.Integer(), nullable=True),
    sa.Column('tag_5_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['editor_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['pointer_id'], ['annotation.id'], ),
    sa.ForeignKeyConstraint(['previous_id'], ['annotation_version.id'], ),
    sa.ForeignKeyConstraint(['tag_1_id'], ['tag.id'], ),
    sa.ForeignKeyConstraint(['tag_2_id'], ['tag.id'], ),
    sa.ForeignKeyConstraint(['tag_3_id'], ['tag.id'], ),
    sa.ForeignKeyConstraint(['tag_4_id'], ['tag.id'], ),
    sa.ForeignKeyConstraint(['tag_5_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_annotation_version_approved'), 'annotation_version', ['approved'], unique=False)
    op.create_index(op.f('ix_annotation_version_book_id'), 'annotation_version', ['book_id'], unique=False)
    op.create_index(op.f('ix_annotation_version_editor_id'), 'annotation_version', ['editor_id'], unique=False)
    op.create_index(op.f('ix_annotation_version_hash_id'), 'annotation_version', ['hash_id'], unique=False)
    op.create_index(op.f('ix_annotation_version_last_line_num'), 'annotation_version', ['last_line_num'], unique=False)
    op.create_index(op.f('ix_annotation_version_modified'), 'annotation_version', ['modified'], unique=False)
    op.create_index(op.f('ix_annotation_version_pointer_id'), 'annotation_version', ['pointer_id'], unique=False)
    op.create_index(op.f('ix_annotation_version_tag_1_id'), 'annotation_version', ['tag_1_id'], unique=False)
    op.create_index(op.f('ix_annotation_version_tag_2_id'), 'annotation_version', ['tag_2_id'], unique=False)
    op.create_index(op.f('ix_annotation_version_tag_3_id'), 'annotation_version', ['tag_3_id'], unique=False)
    op.create_index(op.f('ix_annotation_version_tag_4_id'), 'annotation_version', ['tag_4_id'], unique=False)
    op.create_index(op.f('ix_annotation_version_tag_5_id'), 'annotation_version', ['tag_5_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_annotation_version_tag_5_id'), table_name='annotation_version')
    op.drop_index(op.f('ix_annotation_version_tag_4_id'), table_name='annotation_version')
    op.drop_index(op.f('ix_annotation_version_tag_3_id'), table_name='annotation_version')
    op.drop_index(op.f('ix_annotation_version_tag_2_id'), table_name='annotation_version')
    op.drop_index(op.f('ix_annotation_version_tag_1_id'), table_name='annotation_version')
    op.drop_index(op.f('ix_annotation_version_pointer_id'), table_name='annotation_version')
    op.drop_index(op.f('ix_annotation_version_modified'), table_name='annotation_version')
    op.drop_index(op.f('ix_annotation_version_last_line_num'), table_name='annotation_version')
    op.drop_index(op.f('ix_annotation_version_hash_id'), table_name='annotation_version')
    op.drop_index(op.f('ix_annotation_version_editor_id'), table_name='annotation_version')
    op.drop_index(op.f('ix_annotation_version_book_id'), table_name='annotation_version')
    op.drop_index(op.f('ix_annotation_version_approved'), table_name='annotation_version')
    op.drop_table('annotation_version')
    op.drop_index(op.f('ix_line_pt_num'), table_name='line')
    op.drop_index(op.f('ix_line_l_num'), table_name='line')
    op.drop_index(op.f('ix_line_kind_id'), table_name='line')
    op.drop_index(op.f('ix_line_em_status_id'), table_name='line')
    op.drop_index(op.f('ix_line_ch_num'), table_name='line')
    op.drop_index(op.f('ix_line_book_id'), table_name='line')
    op.drop_index(op.f('ix_line_bk_num'), table_name='line')
    op.drop_table('line')
    op.drop_index(op.f('ix_annotation_edit_pending'), table_name='annotation')
    op.drop_index(op.f('ix_annotation_book_id'), table_name='annotation')
    op.drop_index(op.f('ix_annotation_author_id'), table_name='annotation')
    op.drop_index(op.f('ix_annotation_added'), table_name='annotation')
    op.drop_table('annotation')
    op.drop_index(op.f('ix_book_url'), table_name='book')
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_index(op.f('ix_book_sort_title'), table_name='book')
    op.drop_index(op.f('ix_book_author_id'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_tag_tag'), table_name='tag')
    op.drop_table('tag')
    op.drop_index(op.f('ix_kind_kind'), table_name='kind')
    op.drop_table('kind')
    op.drop_index(op.f('ix_author_url'), table_name='author')
    op.drop_index(op.f('ix_author_name'), table_name='author')
    op.drop_index(op.f('ix_author_last_name'), table_name='author')
    op.drop_index(op.f('ix_author_first_name'), table_name='author')
    op.drop_index(op.f('ix_author_death_date'), table_name='author')
    op.drop_index(op.f('ix_author_birth_date'), table_name='author')
    op.drop_index(op.f('ix_author_added'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###
