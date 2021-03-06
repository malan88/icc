"""empty message

Revision ID: a30c226f1197
Revises: 
Create Date: 2019-05-27 09:05:10.357633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a30c226f1197'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adminright',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enum', sa.String(length=128), nullable=True),
    sa.Column('min_rep', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_adminright_enum'), 'adminright', ['enum'], unique=False)
    op.create_table('annotationflagenum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enum', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_annotationflagenum_enum'), 'annotationflagenum', ['enum'], unique=False)
    op.create_table('commentflagenum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enum', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_commentflagenum_enum'), 'commentflagenum', ['enum'], unique=False)
    op.create_table('lineenum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enum', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lineenum_enum'), 'lineenum', ['enum'], unique=False)
    op.create_table('reputationenum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enum', sa.String(length=128), nullable=True),
    sa.Column('default_delta', sa.Integer(), nullable=False),
    sa.Column('entity', sa.String(length=128), nullable=True),
    sa.Column('display', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reputationenum_enum'), 'reputationenum', ['enum'], unique=False)
    op.create_table('tocenum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enum', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tocenum_enum'), 'tocenum', ['enum'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('displayname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('reputation', sa.Integer(), nullable=True),
    sa.Column('locked', sa.Boolean(), nullable=True),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_displayname'), 'user', ['displayname'], unique=False)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('userflagenum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enum', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_userflagenum_enum'), 'userflagenum', ['enum'], unique=False)
    op.create_table('wiki',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entity_string', sa.String(length=191), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wiki_entity_string'), 'wiki', ['entity_string'], unique=False)
    op.create_table('reputationchange',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('delta', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('enum_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['enum_id'], ['reputationenum.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rights',
    sa.Column('right_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['right_id'], ['adminright.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=128), nullable=True),
    sa.Column('locked', sa.Boolean(), nullable=True),
    sa.Column('wiki_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['wiki_id'], ['wiki.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tag_tag'), 'tag', ['tag'], unique=True)
    op.create_table('tagrequest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=127), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('rejected', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('wiki_id', sa.Integer(), nullable=False),
    sa.Column('requester_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['requester_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['wiki_id'], ['wiki.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tagrequest_approved'), 'tagrequest', ['approved'], unique=False)
    op.create_index(op.f('ix_tagrequest_rejected'), 'tagrequest', ['rejected'], unique=False)
    op.create_index(op.f('ix_tagrequest_requester_id'), 'tagrequest', ['requester_id'], unique=False)
    op.create_index(op.f('ix_tagrequest_tag'), 'tagrequest', ['tag'], unique=False)
    op.create_index(op.f('ix_tagrequest_timestamp'), 'tagrequest', ['timestamp'], unique=False)
    op.create_index(op.f('ix_tagrequest_weight'), 'tagrequest', ['weight'], unique=False)
    op.create_table('text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('sort_title', sa.String(length=128), nullable=True),
    sa.Column('wiki_id', sa.Integer(), nullable=False),
    sa.Column('published', sa.Date(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['wiki_id'], ['wiki.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_text_sort_title'), 'text', ['sort_title'], unique=False)
    op.create_index(op.f('ix_text_title'), 'text', ['title'], unique=False)
    op.create_table('textrequest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=127), nullable=True),
    sa.Column('authors', sa.String(length=127), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('rejected', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('wiki_id', sa.Integer(), nullable=False),
    sa.Column('requester_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['requester_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['wiki_id'], ['wiki.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_textrequest_approved'), 'textrequest', ['approved'], unique=False)
    op.create_index(op.f('ix_textrequest_authors'), 'textrequest', ['authors'], unique=False)
    op.create_index(op.f('ix_textrequest_rejected'), 'textrequest', ['rejected'], unique=False)
    op.create_index(op.f('ix_textrequest_requester_id'), 'textrequest', ['requester_id'], unique=False)
    op.create_index(op.f('ix_textrequest_timestamp'), 'textrequest', ['timestamp'], unique=False)
    op.create_index(op.f('ix_textrequest_title'), 'textrequest', ['title'], unique=False)
    op.create_index(op.f('ix_textrequest_weight'), 'textrequest', ['weight'], unique=False)
    op.create_table('user_flrs',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('userflag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('thrower_id', sa.Integer(), nullable=True),
    sa.Column('resolver_id', sa.Integer(), nullable=True),
    sa.Column('time_thrown', sa.DateTime(), nullable=True),
    sa.Column('time_resolved', sa.DateTime(), nullable=True),
    sa.Column('enum_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enum_id'], ['userflagenum.id'], ),
    sa.ForeignKeyConstraint(['resolver_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['thrower_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_userflag_enum_id'), 'userflag', ['enum_id'], unique=False)
    op.create_index(op.f('ix_userflag_resolver_id'), 'userflag', ['resolver_id'], unique=False)
    op.create_index(op.f('ix_userflag_thrower_id'), 'userflag', ['thrower_id'], unique=False)
    op.create_index(op.f('ix_userflag_user_id'), 'userflag', ['user_id'], unique=False)
    op.create_table('wikiedit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('current', sa.Boolean(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('rejected', sa.Boolean(), nullable=True),
    sa.Column('reason', sa.String(length=191), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.Column('editor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['editor_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['entity_id'], ['wiki.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wikiedit_approved'), 'wikiedit', ['approved'], unique=False)
    op.create_index(op.f('ix_wikiedit_current'), 'wikiedit', ['current'], unique=False)
    op.create_index(op.f('ix_wikiedit_rejected'), 'wikiedit', ['rejected'], unique=False)
    op.create_index(op.f('ix_wikiedit_timestamp'), 'wikiedit', ['timestamp'], unique=False)
    op.create_table('writer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('family_name', sa.String(length=128), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('death_date', sa.Date(), nullable=True),
    sa.Column('wiki_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['wiki_id'], ['wiki.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_writer_birth_date'), 'writer', ['birth_date'], unique=False)
    op.create_index(op.f('ix_writer_death_date'), 'writer', ['death_date'], unique=False)
    op.create_index(op.f('ix_writer_family_name'), 'writer', ['family_name'], unique=False)
    op.create_index(op.f('ix_writer_name'), 'writer', ['name'], unique=False)
    op.create_index(op.f('ix_writer_timestamp'), 'writer', ['timestamp'], unique=False)
    op.create_table('edition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('_title', sa.String(length=235), nullable=True),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('text_id', sa.Integer(), nullable=True),
    sa.Column('primary', sa.Boolean(), nullable=True),
    sa.Column('wiki_id', sa.Integer(), nullable=False),
    sa.Column('published', sa.DateTime(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('tochide', sa.Boolean(), nullable=True),
    sa.Column('verse', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['text_id'], ['text.id'], ),
    sa.ForeignKeyConstraint(['wiki_id'], ['wiki.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag_followers',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('tagrequest_followers',
    sa.Column('tagrequest_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tagrequest_id'], ['tagrequest.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('tagrequestvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('delta', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('tag_request_id', sa.Integer(), nullable=True),
    sa.Column('voter_id', sa.Integer(), nullable=True),
    sa.Column('reputationchange_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['reputationchange_id'], ['reputationchange.id'], ),
    sa.ForeignKeyConstraint(['tag_request_id'], ['tagrequest.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tagrequestvote_tag_request_id'), 'tagrequestvote', ['tag_request_id'], unique=False)
    op.create_table('text_followers',
    sa.Column('text_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['text_id'], ['text.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('textrequest_followers',
    sa.Column('textrequest_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['textrequest_id'], ['textrequest.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('textrequestvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('delta', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('text_request_id', sa.Integer(), nullable=True),
    sa.Column('voter_id', sa.Integer(), nullable=True),
    sa.Column('reputationchange_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['reputationchange_id'], ['reputationchange.id'], ),
    sa.ForeignKeyConstraint(['text_request_id'], ['textrequest.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_textrequestvote_text_request_id'), 'textrequestvote', ['text_request_id'], unique=False)
    op.create_table('wikieditvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('delta', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('edit_id', sa.Integer(), nullable=False),
    sa.Column('voter_id', sa.Integer(), nullable=True),
    sa.Column('reputationchange_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['edit_id'], ['wikiedit.id'], ),
    sa.ForeignKeyConstraint(['reputationchange_id'], ['reputationchange.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wikieditvote_edit_id'), 'wikieditvote', ['edit_id'], unique=False)
    op.create_table('writer_followers',
    sa.Column('writer_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['writer_id'], ['writer.id'], )
    )
    op.create_table('annotation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('annotator_id', sa.Integer(), nullable=True),
    sa.Column('edition_id', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('locked', sa.Boolean(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['annotator_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['edition_id'], ['edition.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_annotation_annotator_id'), 'annotation', ['annotator_id'], unique=False)
    op.create_index(op.f('ix_annotation_edition_id'), 'annotation', ['edition_id'], unique=False)
    op.create_index(op.f('ix_annotation_locked'), 'annotation', ['locked'], unique=False)
    op.create_index(op.f('ix_annotation_timestamp'), 'annotation', ['timestamp'], unique=False)
    op.create_table('edition_followers',
    sa.Column('edition_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['edition_id'], ['edition.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('toc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('precedence', sa.Integer(), nullable=True),
    sa.Column('body', sa.String(length=200), nullable=True),
    sa.Column('haslines', sa.Boolean(), nullable=True),
    sa.Column('prev_id', sa.Integer(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('edition_id', sa.Integer(), nullable=True),
    sa.Column('enum_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['edition_id'], ['edition.id'], ),
    sa.ForeignKeyConstraint(['enum_id'], ['tocenum.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['toc.id'], ),
    sa.ForeignKeyConstraint(['prev_id'], ['toc.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_toc_body'), 'toc', ['body'], unique=False)
    op.create_index(op.f('ix_toc_edition_id'), 'toc', ['edition_id'], unique=False)
    op.create_index(op.f('ix_toc_enum_id'), 'toc', ['enum_id'], unique=False)
    op.create_index(op.f('ix_toc_haslines'), 'toc', ['haslines'], unique=False)
    op.create_index(op.f('ix_toc_num'), 'toc', ['num'], unique=False)
    op.create_index(op.f('ix_toc_parent_id'), 'toc', ['parent_id'], unique=False)
    op.create_index(op.f('ix_toc_precedence'), 'toc', ['precedence'], unique=False)
    op.create_index(op.f('ix_toc_prev_id'), 'toc', ['prev_id'], unique=False)
    op.create_table('writerconnection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('writer_id', sa.Integer(), nullable=True),
    sa.Column('edition_id', sa.Integer(), nullable=True),
    sa.Column('enum_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['edition_id'], ['edition.id'], ),
    sa.ForeignKeyConstraint(['writer_id'], ['writer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('annotation_followers',
    sa.Column('annotation_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['annotation_id'], ['annotation.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('annotationflag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('annotation_id', sa.Integer(), nullable=True),
    sa.Column('thrower_id', sa.Integer(), nullable=True),
    sa.Column('resolver_id', sa.Integer(), nullable=True),
    sa.Column('time_thrown', sa.DateTime(), nullable=True),
    sa.Column('time_resolved', sa.DateTime(), nullable=True),
    sa.Column('enum_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['annotation_id'], ['annotation.id'], ),
    sa.ForeignKeyConstraint(['enum_id'], ['annotationflagenum.id'], ),
    sa.ForeignKeyConstraint(['resolver_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['thrower_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_annotationflag_annotation_id'), 'annotationflag', ['annotation_id'], unique=False)
    op.create_index(op.f('ix_annotationflag_enum_id'), 'annotationflag', ['enum_id'], unique=False)
    op.create_index(op.f('ix_annotationflag_resolver_id'), 'annotationflag', ['resolver_id'], unique=False)
    op.create_index(op.f('ix_annotationflag_thrower_id'), 'annotationflag', ['thrower_id'], unique=False)
    op.create_table('annotationvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('delta', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('annotation_id', sa.Integer(), nullable=True),
    sa.Column('voter_id', sa.Integer(), nullable=True),
    sa.Column('reputationchange_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['annotation_id'], ['annotation.id'], ),
    sa.ForeignKeyConstraint(['reputationchange_id'], ['reputationchange.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_annotationvote_annotation_id'), 'annotationvote', ['annotation_id'], unique=False)
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('poster_id', sa.Integer(), nullable=False),
    sa.Column('annotation_id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('depth', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['annotation_id'], ['annotation.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['comment.id'], ),
    sa.ForeignKeyConstraint(['poster_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_annotation_id'), 'comment', ['annotation_id'], unique=False)
    op.create_index(op.f('ix_comment_parent_id'), 'comment', ['parent_id'], unique=False)
    op.create_index(op.f('ix_comment_poster_id'), 'comment', ['poster_id'], unique=False)
    op.create_table('line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('em_id', sa.Integer(), nullable=True),
    sa.Column('toc_id', sa.Integer(), nullable=True),
    sa.Column('edition_id', sa.Integer(), nullable=True),
    sa.Column('enum_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['edition_id'], ['edition.id'], ),
    sa.ForeignKeyConstraint(['enum_id'], ['lineenum.id'], ),
    sa.ForeignKeyConstraint(['toc_id'], ['toc.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_line_edition_id'), 'line', ['edition_id'], unique=False)
    op.create_index(op.f('ix_line_enum_id'), 'line', ['enum_id'], unique=False)
    op.create_index(op.f('ix_line_num'), 'line', ['num'], unique=False)
    op.create_index(op.f('ix_line_toc_id'), 'line', ['toc_id'], unique=False)
    op.create_table('commentflag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=True),
    sa.Column('thrower_id', sa.Integer(), nullable=True),
    sa.Column('resolver_id', sa.Integer(), nullable=True),
    sa.Column('time_thrown', sa.DateTime(), nullable=True),
    sa.Column('time_resolved', sa.DateTime(), nullable=True),
    sa.Column('enum_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['entity_id'], ['comment.id'], ),
    sa.ForeignKeyConstraint(['enum_id'], ['commentflagenum.id'], ),
    sa.ForeignKeyConstraint(['resolver_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['thrower_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_commentflag_entity_id'), 'commentflag', ['entity_id'], unique=False)
    op.create_index(op.f('ix_commentflag_enum_id'), 'commentflag', ['enum_id'], unique=False)
    op.create_index(op.f('ix_commentflag_resolver_id'), 'commentflag', ['resolver_id'], unique=False)
    op.create_index(op.f('ix_commentflag_thrower_id'), 'commentflag', ['thrower_id'], unique=False)
    op.create_table('commentvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('delta', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('entity_id', sa.Integer(), nullable=True),
    sa.Column('voter_id', sa.Integer(), nullable=True),
    sa.Column('reputationchange_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['entity_id'], ['comment.id'], ),
    sa.ForeignKeyConstraint(['reputationchange_id'], ['reputationchange.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_commentvote_entity_id'), 'commentvote', ['entity_id'], unique=False)
    op.create_table('edit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('current', sa.Boolean(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('rejected', sa.Boolean(), nullable=True),
    sa.Column('reason', sa.String(length=191), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('edition_id', sa.Integer(), nullable=True),
    sa.Column('entity_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('first_line_num', sa.Integer(), nullable=True),
    sa.Column('last_line_num', sa.Integer(), nullable=True),
    sa.Column('first_char_idx', sa.Integer(), nullable=True),
    sa.Column('last_char_idx', sa.Integer(), nullable=True),
    sa.Column('editor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['edition_id'], ['edition.id'], ),
    sa.ForeignKeyConstraint(['editor_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['entity_id'], ['annotation.id'], ),
    sa.ForeignKeyConstraint(['first_line_num'], ['line.num'], ),
    sa.ForeignKeyConstraint(['last_line_num'], ['line.num'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_edit_approved'), 'edit', ['approved'], unique=False)
    op.create_index(op.f('ix_edit_current'), 'edit', ['current'], unique=False)
    op.create_index(op.f('ix_edit_edition_id'), 'edit', ['edition_id'], unique=False)
    op.create_index(op.f('ix_edit_entity_id'), 'edit', ['entity_id'], unique=False)
    op.create_index(op.f('ix_edit_last_line_num'), 'edit', ['last_line_num'], unique=False)
    op.create_index(op.f('ix_edit_rejected'), 'edit', ['rejected'], unique=False)
    op.create_table('editvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('delta', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('edit_id', sa.Integer(), nullable=True),
    sa.Column('voter_id', sa.Integer(), nullable=True),
    sa.Column('reputationchange_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['edit_id'], ['edit.id'], ),
    sa.ForeignKeyConstraint(['reputationchange_id'], ['reputationchange.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_editvote_edit_id'), 'editvote', ['edit_id'], unique=False)
    op.create_table('tags',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('edit_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['edit_id'], ['edit.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    op.drop_index(op.f('ix_editvote_edit_id'), table_name='editvote')
    op.drop_table('editvote')
    op.drop_index(op.f('ix_edit_rejected'), table_name='edit')
    op.drop_index(op.f('ix_edit_last_line_num'), table_name='edit')
    op.drop_index(op.f('ix_edit_entity_id'), table_name='edit')
    op.drop_index(op.f('ix_edit_edition_id'), table_name='edit')
    op.drop_index(op.f('ix_edit_current'), table_name='edit')
    op.drop_index(op.f('ix_edit_approved'), table_name='edit')
    op.drop_table('edit')
    op.drop_index(op.f('ix_commentvote_entity_id'), table_name='commentvote')
    op.drop_table('commentvote')
    op.drop_index(op.f('ix_commentflag_thrower_id'), table_name='commentflag')
    op.drop_index(op.f('ix_commentflag_resolver_id'), table_name='commentflag')
    op.drop_index(op.f('ix_commentflag_enum_id'), table_name='commentflag')
    op.drop_index(op.f('ix_commentflag_entity_id'), table_name='commentflag')
    op.drop_table('commentflag')
    op.drop_index(op.f('ix_line_toc_id'), table_name='line')
    op.drop_index(op.f('ix_line_num'), table_name='line')
    op.drop_index(op.f('ix_line_enum_id'), table_name='line')
    op.drop_index(op.f('ix_line_edition_id'), table_name='line')
    op.drop_table('line')
    op.drop_index(op.f('ix_comment_poster_id'), table_name='comment')
    op.drop_index(op.f('ix_comment_parent_id'), table_name='comment')
    op.drop_index(op.f('ix_comment_annotation_id'), table_name='comment')
    op.drop_table('comment')
    op.drop_index(op.f('ix_annotationvote_annotation_id'), table_name='annotationvote')
    op.drop_table('annotationvote')
    op.drop_index(op.f('ix_annotationflag_thrower_id'), table_name='annotationflag')
    op.drop_index(op.f('ix_annotationflag_resolver_id'), table_name='annotationflag')
    op.drop_index(op.f('ix_annotationflag_enum_id'), table_name='annotationflag')
    op.drop_index(op.f('ix_annotationflag_annotation_id'), table_name='annotationflag')
    op.drop_table('annotationflag')
    op.drop_table('annotation_followers')
    op.drop_table('writerconnection')
    op.drop_index(op.f('ix_toc_prev_id'), table_name='toc')
    op.drop_index(op.f('ix_toc_precedence'), table_name='toc')
    op.drop_index(op.f('ix_toc_parent_id'), table_name='toc')
    op.drop_index(op.f('ix_toc_num'), table_name='toc')
    op.drop_index(op.f('ix_toc_haslines'), table_name='toc')
    op.drop_index(op.f('ix_toc_enum_id'), table_name='toc')
    op.drop_index(op.f('ix_toc_edition_id'), table_name='toc')
    op.drop_index(op.f('ix_toc_body'), table_name='toc')
    op.drop_table('toc')
    op.drop_table('edition_followers')
    op.drop_index(op.f('ix_annotation_timestamp'), table_name='annotation')
    op.drop_index(op.f('ix_annotation_locked'), table_name='annotation')
    op.drop_index(op.f('ix_annotation_edition_id'), table_name='annotation')
    op.drop_index(op.f('ix_annotation_annotator_id'), table_name='annotation')
    op.drop_table('annotation')
    op.drop_table('writer_followers')
    op.drop_index(op.f('ix_wikieditvote_edit_id'), table_name='wikieditvote')
    op.drop_table('wikieditvote')
    op.drop_index(op.f('ix_textrequestvote_text_request_id'), table_name='textrequestvote')
    op.drop_table('textrequestvote')
    op.drop_table('textrequest_followers')
    op.drop_table('text_followers')
    op.drop_index(op.f('ix_tagrequestvote_tag_request_id'), table_name='tagrequestvote')
    op.drop_table('tagrequestvote')
    op.drop_table('tagrequest_followers')
    op.drop_table('tag_followers')
    op.drop_table('edition')
    op.drop_index(op.f('ix_writer_timestamp'), table_name='writer')
    op.drop_index(op.f('ix_writer_name'), table_name='writer')
    op.drop_index(op.f('ix_writer_family_name'), table_name='writer')
    op.drop_index(op.f('ix_writer_death_date'), table_name='writer')
    op.drop_index(op.f('ix_writer_birth_date'), table_name='writer')
    op.drop_table('writer')
    op.drop_index(op.f('ix_wikiedit_timestamp'), table_name='wikiedit')
    op.drop_index(op.f('ix_wikiedit_rejected'), table_name='wikiedit')
    op.drop_index(op.f('ix_wikiedit_current'), table_name='wikiedit')
    op.drop_index(op.f('ix_wikiedit_approved'), table_name='wikiedit')
    op.drop_table('wikiedit')
    op.drop_index(op.f('ix_userflag_user_id'), table_name='userflag')
    op.drop_index(op.f('ix_userflag_thrower_id'), table_name='userflag')
    op.drop_index(op.f('ix_userflag_resolver_id'), table_name='userflag')
    op.drop_index(op.f('ix_userflag_enum_id'), table_name='userflag')
    op.drop_table('userflag')
    op.drop_table('user_flrs')
    op.drop_index(op.f('ix_textrequest_weight'), table_name='textrequest')
    op.drop_index(op.f('ix_textrequest_title'), table_name='textrequest')
    op.drop_index(op.f('ix_textrequest_timestamp'), table_name='textrequest')
    op.drop_index(op.f('ix_textrequest_requester_id'), table_name='textrequest')
    op.drop_index(op.f('ix_textrequest_rejected'), table_name='textrequest')
    op.drop_index(op.f('ix_textrequest_authors'), table_name='textrequest')
    op.drop_index(op.f('ix_textrequest_approved'), table_name='textrequest')
    op.drop_table('textrequest')
    op.drop_index(op.f('ix_text_title'), table_name='text')
    op.drop_index(op.f('ix_text_sort_title'), table_name='text')
    op.drop_table('text')
    op.drop_index(op.f('ix_tagrequest_weight'), table_name='tagrequest')
    op.drop_index(op.f('ix_tagrequest_timestamp'), table_name='tagrequest')
    op.drop_index(op.f('ix_tagrequest_tag'), table_name='tagrequest')
    op.drop_index(op.f('ix_tagrequest_requester_id'), table_name='tagrequest')
    op.drop_index(op.f('ix_tagrequest_rejected'), table_name='tagrequest')
    op.drop_index(op.f('ix_tagrequest_approved'), table_name='tagrequest')
    op.drop_table('tagrequest')
    op.drop_index(op.f('ix_tag_tag'), table_name='tag')
    op.drop_table('tag')
    op.drop_table('rights')
    op.drop_table('reputationchange')
    op.drop_index(op.f('ix_wiki_entity_string'), table_name='wiki')
    op.drop_table('wiki')
    op.drop_index(op.f('ix_userflagenum_enum'), table_name='userflagenum')
    op.drop_table('userflagenum')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_displayname'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_tocenum_enum'), table_name='tocenum')
    op.drop_table('tocenum')
    op.drop_index(op.f('ix_reputationenum_enum'), table_name='reputationenum')
    op.drop_table('reputationenum')
    op.drop_index(op.f('ix_lineenum_enum'), table_name='lineenum')
    op.drop_table('lineenum')
    op.drop_index(op.f('ix_commentflagenum_enum'), table_name='commentflagenum')
    op.drop_table('commentflagenum')
    op.drop_index(op.f('ix_annotationflagenum_enum'), table_name='annotationflagenum')
    op.drop_table('annotationflagenum')
    op.drop_index(op.f('ix_adminright_enum'), table_name='adminright')
    op.drop_table('adminright')
    # ### end Alembic commands ###
