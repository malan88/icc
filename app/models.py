import hashlib
from math import log10 as l
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db, login
from sqlalchemy import or_, func
from flask import url_for

####################
## User Functions ##
####################

conferred_right = db.Table(
        "conferred_rights",
        db.Column("right_id", db.Integer, db.ForeignKey("admin_right.id")),
        db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
        )

class AdminRight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    right = db.Column(db.String(128), index=True)

    def __repr__(self):
        return self.right

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    reputation = db.Column(db.Integer, default=0)
    cumulative_negative = db.Column(db.Integer, default=0)
    cumulative_positive = db.Column(db.Integer, default=0)
    locked = db.Column(db.Boolean, default=False)
    votes = db.relationship("Annotation", secondary="vote",
            primaryjoin="User.id==vote.c.user_id",
            secondaryjoin="Annotation.id==vote.c.annotation_id",
            backref="voters")
    edit_votes = db.relationship("AnnotationVersion", secondary="edit_vote",
            primaryjoin="User.id==edit_vote.c.user_id",
            secondaryjoin="AnnotationVersion.id==edit_vote.c.edit_id",
            backref="edit_voters")
    rights = db.relationship("AdminRight", secondary=conferred_right,
            backref="admins")

    def in_rights(self, right):
        r = AdminRight.query.filter_by(right=right).first()
        return r

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def upvote(self):
        self.reputation += 5
        self.cumulative_positive += 5

    def rollback_upvote(self):
        self.reputation -= 5
        if self.reputation <= 0:
            self.reputation = 0
        self.cumulative_positive -= 5

    def downvote(self):
        self.reputation -= 2
        if self.reputation <= 0:
            self.reputation = 0
        self.cumulative_negative -= 2

    def rollback_downvote(self):
        self.reputation += 2
        self.cumulative_negative += 2

    def already_voted(self, annotation):
        if annotation in self.votes:
            return True
        else:
            return False

    def get_vote(self, annotation):
        return Vote.query.filter(Vote.annotation==annotation,
                Vote.user==self).first()

    def get_vote_dict(self):
        v = {}
        for vote in self.ballots:
            v[vote.annotation.id] = vote.is_up()
        return v

    def get_edit_vote(self, edit):
        return EditVote.query.filter(EditVote.edit==edit,
                EditVote.user==self).first()

    def up_power(self):
        if self.reputation <= 10:
            return 1
        elif self.reputation == 10**int(l(self.reputation)):
            log = int(l(self.reputation) - (l(11) - int(l(11))))
            return int(self.reputation / 10**log) + 10*log - 10
        log = int(l(self.reputation))
        return int(self.reputation / 10**log) + 10*log - 10

    def down_power(self):
        if self.reputation <= 10:
            return 1
        return round(self.up_power() / 2)

    def authorize(self, min_rep):
        if self.reputation < min_rep:
            abort(403)

    def is_authorized(self, min_rep):
        if self.reputation >= min_rep:
            return True
        else:
            return False

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


###########
## Votes ##
###########

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), index=True)
    user = db.relationship("User", backref="ballots")
    annotation_id = db.Column(db.Integer, db.ForeignKey("annotation.id"),
            index=True)
    annotation = db.relationship("Annotation", backref="ballots")
    delta = db.Column(db.Integer)

    def __repr__(self):
        return f"<{self.user.username} {self.delta} on {self.annotation}>"

    def is_up(self):
        if self.delta > 0:
            return True
        else:
            return False

class EditVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), index=True)
    user = db.relationship("User", backref="edit_ballots")
    edit_id = db.Column(db.Integer, db.ForeignKey("annotation_version.id"),
            index=True)
    edit = db.relationship("AnnotationVersion", backref="edit_ballots")
    delta = db.Column(db.Integer)

    def __repr__(self):
        return f"<{self.user.username} {self.delta} on {self.edit}>"

    def is_up(self):
        if self.delta > 0:
            return True
        else:
            return False

###############
## Meta Data ##
###############

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    first_name = db.Column(db.String(128), index=True)
    last_name = db.Column(db.String(128), index=True)
    url = db.Column(db.String(128), index=True)
    birth_date = db.Column(db.Date, index=True)
    death_date = db.Column(db.Date, index=True)
    bio = db.Column(db.Text)
    added = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Author: {self.name}>"

    def book_count(self):
        cnt = Book.query.filter_by(author=self).count()
        return cnt


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    sort_title = db.Column(db.String(128), index=True)
    url = db.Column(db.String(128), index=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), index=True)
    author = db.relationship("Author", backref="books")
    summary = db.Column(db.Text)
    published = db.Column(db.Date)
    added = db.Column(db.DateTime)

    def line_count(self):
        cnt = Line.query.filter_by(book=self).count()
        return cnt

    def annotation_count(self):
        cnt = Annotation.query.filter_by(book=self).count()
        return cnt

    def __repr__(self):
        return f"<Book {self.id}: {self.title} by {self.author}>"

class Kind(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(12), index=True)

    def __repr__(self):
        return f"<k {self.id}: {self.kind}>"

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(128), index=True, unique=True)
    admin = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Tag {self.id}: {self.tag}>"

    def get_annotations(self):
        edits = AnnotationVersion.query.filter(or_(
            AnnotationVersion.tag_1_id==self.id,
            AnnotationVersion.tag_2_id==self.id,
            AnnotationVersion.tag_3_id==self.id,
            AnnotationVersion.tag_4_id==self.id,
            AnnotationVersion.tag_5_id==self.id)
            ).order_by(AnnotationVersion.modified.desc()).all()
        annotations = []
        for e in edits:
            if self in e.pointer.get_tags() and e.pointer not in annotations:
                annotations.append(e.pointer)
        return annotations

    def get_annotations_by_book(self, book):
        edits = AnnotationVersion.query.filter(or_(
            AnnotationVersion.tag_1_id==self.id,
            AnnotationVersion.tag_2_id==self.id,
            AnnotationVersion.tag_3_id==self.id,
            AnnotationVersion.tag_4_id==self.id,
            AnnotationVersion.tag_5_id==self.id),
            AnnotationVersion.book_id==book.id
            ).order_by(AnnotationVersion.last_line_num.desc()).all()
        annotations = []
        for e in edits:
            if self in e.pointer.get_tags() and e.pointer not in annotations:
                annotations.append(e.pointer)
        return annotations

    def get_count(self):
        annotations = self.get_annotations()
        return len(annotations)




####################
## Content Models ##
####################

class Line(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), index=True)
    book = db.relationship("Book", backref="lines")

    l_num = db.Column(db.Integer, index=True)

    kind_id = db.Column(db.Integer, db.ForeignKey("kind.id"), index=True)
    kind = db.relationship("Kind", foreign_keys=[kind_id])

    bk_num = db.Column(db.Integer, index=True)
    pt_num = db.Column(db.Integer, index=True)
    ch_num = db.Column(db.Integer, index=True)

    em_status_id = db.Column(db.Integer, db.ForeignKey("kind.id"), index=True)
    em_status = db.relationship("Kind", foreign_keys=[em_status_id])

    line = db.Column(db.String(200))

    def __repr__(self):
        return f"<l {self.id}: {self.l_num} of {self.book.title} [{self.kind.kind}]>"

    def get_prev_section(self):     # cleverer than expected
        if self.ch_num != 0:        # decrementing by chapters
            lines = Line.query.filter(Line.book_id==self.book_id,
                    Line.l_num<self.l_num).order_by(Line.l_num.desc()
                            ).limit(10).all()
            for l in lines:         # go backwards through lines
                if l.ch_num != 0:   # the 1st time ch_num != 0, return it
                    return l
        elif self.pt_num != 0:      # decrementing by parts
            lines = Line.query.filter(Line.book_id==self.book_id,
                    Line.ch_num==0, Line.l_num<self.l_num
                    ).order_by(Line.l_num.desc()).limit(10).all()
            for l in lines:
                if l.pt_num != 0:
                    return l
        else:                       # decrementing by books
            lines = Line.query.filter(Line.book_id==self.book_id,
                    Line.ch_num==0, Line.pt_num==0, Line.l_num<self.l_num
                    ).order_by(Line.l_num.desc()).limit(10).all()
            for l in lines:
                if l.bk_num != 0:
                    return l
        return None                 # there is no previous section

    def get_next_section(self):
        if self.ch_num != 0:
            lines = Line.query.filter(Line.book_id==self.book_id,
                    Line.l_num>self.l_num
                    ).order_by(Line.l_num.asc()).limit(10).all()
            for l in lines:
                if l.ch_num != 0:
                    return l
        elif self.pt_num != 0:
            lines = Line.query.filter(Line.book_id==self.book_id,
                    Line.ch_num==0, Line.l_num>self.l_num
                    ).order_by(Line.l_num.asc()).limit(10).all()
            for l in lines:
                if l.pt_num != 0:
                    return l
        else:
            lines = Line.query.filter(Line.book_id==self.book_id,
                    Line.ch_num==0, Line.pt_num==0, Line.l_num>self.l_num
                    ).order_by(Line.l_num.asc()).limit(10).all()
            for l in lines:
                if l.bk_num != 0:
                    return l
        return None


    def get_url(self):
        return url_for("read", book_url=self.book.url, bk=self.bk_num,
                pt=self.pt_num, ch=self.ch_num)



class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), index=True)
    author = db.relationship("User", backref="annotations")

    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), index=True)
    book = db.relationship("Book", backref="annotations")

    head_id = db.Column(db.Integer, db.ForeignKey("annotation_version.id"))
    HEAD = db.relationship("AnnotationVersion", foreign_keys=[head_id])

    weight = db.Column(db.Integer, default=0)

    added = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    edit_pending = db.Column(db.Boolean, index=True, default=False)

    def upvote(self, voter):
        weight = voter.up_power()
        self.weight += weight
        self.author.upvote()
        vote = Vote(user=voter, annotation=self, delta=weight)
        db.session.add(vote)

    def downvote(self, voter):
        weight = voter.down_power()
        weight = -weight
        self.weight += weight
        self.author.downvote()
        vote = Vote(user=voter, annotation=self, delta=weight)
        db.session.add(vote)

    def rollback(self, vote):
        self.weight -= vote.delta
        if vote.is_up():
            self.author.rollback_upvote()
        else:
            self.author.rollback_downvote()
        db.session.delete(vote)

    def get_tags(self):
        tags = []
        if self.HEAD.tag_1:
            tags.append(self.HEAD.tag_1)
        if self.HEAD.tag_2:
            tags.append(self.HEAD.tag_2)
        if self.HEAD.tag_3:
            tags.append(self.HEAD.tag_3)
        if self.HEAD.tag_4:
            tags.append(self.HEAD.tag_4)
        if self.HEAD.tag_5:
            tags.append(self.HEAD.tag_5)
        return tags

###########
## Edits ##
###########

class AnnotationVersion(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    editor_id = db.Column(db.Integer, db.ForeignKey("user.id"), index=True)
    editor = db.relationship("User")

    weight = db.Column(db.Integer, default=0)
    approved = db.Column(db.Boolean, default=False, index=True)
    rejected = db.Column(db.Boolean, default=False, index=True)

    pointer_id = db.Column(db.Integer, db.ForeignKey("annotation.id"), index=True)
    pointer = db.relationship("Annotation", foreign_keys=[pointer_id])

    hash_id = db.Column(db.String(40), index=True)

    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), index=True)
    book = db.relationship("Book")

    previous_id = db.Column(db.Integer, db.ForeignKey("annotation_version.id"),
            default=None)
    previous = db.relationship("AnnotationVersion")

    first_line_num = db.Column(db.Integer)
    last_line_num = db.Column(db.Integer, index=True)
    first_char_idx = db.Column(db.Integer)
    last_char_idx = db.Column(db.Integer)

    annotation = db.Column(db.Text)

    modified = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    tag_1_id = db.Column(db.Integer, db.ForeignKey("tag.id"), index=True)
    tag_2_id = db.Column(db.Integer, db.ForeignKey("tag.id"), index=True)
    tag_3_id = db.Column(db.Integer, db.ForeignKey("tag.id"), index=True)
    tag_4_id = db.Column(db.Integer, db.ForeignKey("tag.id"), index=True)
    tag_5_id = db.Column(db.Integer, db.ForeignKey("tag.id"), index=True)

    tag_1 = db.relationship("Tag", foreign_keys=[tag_1_id])
    tag_2 = db.relationship("Tag", foreign_keys=[tag_2_id])
    tag_3 = db.relationship("Tag", foreign_keys=[tag_3_id])
    tag_4 = db.relationship("Tag", foreign_keys=[tag_4_id])
    tag_5 = db.relationship("Tag", foreign_keys=[tag_5_id])


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        s = f"{self.book_id}," \
                f"{self.first_line_num},{self.last_line_num}," \
                f"{self.first_char_idx},{self.last_char_idx}," \
                f"{self.annotation},{self.tag_1},{self.tag_2},{self.tag_3}," \
                f"{self.tag_4},{self.tag_5}" 
        self.hash_id = hashlib.sha1(s.encode("utf8")).hexdigest()

    def __repr__(self):
        return f"<Ann {self.id} on book {self.book.title}>"

    def get_lines(self):
        lines = Line.query.filter(Line.book_id==self.book_id,
                Line.l_num >= self.first_line_num, 
                Line.l_num <= self.last_line_num).all()
        return lines

    def get_hl(self):
        lines = self.get_lines()

        if self.first_line_num == self.last_line_num: 
            lines[0].line = lines[0].line[self.first_char_idx:self.last_char_idx]
        else:
            lines[0].line = lines[0].line[self.first_char_idx:]
            lines[-1].line = lines[-1].line[:self.last_char_idx]

        return lines

    def approve(self, voter):
        self.weight += 1
        vote = EditVote(user=voter, edit=self, delta=1)
        db.session.add(vote)

    def reject(self, voter):
        self.weight -= 1
        vote = EditVote(user=voter, edit=self, delta=-1)
        db.session.add(vote)
