from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Page(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), index = True)
    book = db.relationship("Book", backref="pages")
    page = db.Column(db.Text)
    page_num = db.Column(db.Integer)

    def __repr__(self):
        return f"<p. {self.page_num} of {self.book.title} by {self.book.author.name}>"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128), index = True)
    url = db.Column(db.String(128), index = True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), index = True)
    author = db.relationship("Author", backref="books")
    published = db.Column(db.Date)
    ts_added = db.Column(db.DateTime)
    meta_data = db.Column(db.Text)
    sort_name = db.Column(db.String(128), index = True)

    def __repr__(self):
        return f"<Book: {self.title} by {self.author}>"


class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), index = True)
    first_name = db.Column(db.String(128), index = True)
    last_name = db.Column(db.String(128), index = True)
    url = db.Column(db.String(128), index = True)
    birth_date = db.Column(db.Date, index = True)
    death_date = db.Column(db.Date, index = True)
    ts_added = db.Column(db.DateTime, index = True, default = datetime.utcnow)

    def __repr__(self):
        return f"<Author: {self.name}>"

class Break(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), index = True)
    book = db.relationship("Book", backref="breaks")
    book_num = db.Column(db.Integer, index = True)
    part_num = db.Column(db.Integer, index = True)
    ch_num = db.Column(db.Integer, index = True)
    page_num = db.Column(db.Integer, index = True)
    break_title = db.Column(db.Text)

    def __repr__(self):
        if book_num:
            if part_num:
                if ch_num:
                    return f'<Book {book_num}, Part {part_num}, Ch {ch_num}>'
                else:
                    return f'<Book {book_num}, Part {part_num}>'
            else:
                if ch_num:
                    return f'<Book {book_num}, Ch {ch_num}>'
                else:
                    return f'<Book {book_num}>'
        else:
            if part_num:
                if ch_num:
                    return f'<Part {part_num}, Ch {ch_num}>'
                else:
                    return f'<Part {part_num}>'
            else:
                return f'<Ch {ch_num}>'
