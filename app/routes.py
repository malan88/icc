from flask import render_template, flash, redirect, url_for, request, Markup
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User, Book, Author, Page


@app.route('/')
@app.route('/index/')
def index():
    books = Book.query.all()
    authors = Author.query.all()
    return render_template('index.html', title='Home', books = books, 
            authors = authors)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)



@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route('/author/<name>/')
def author(name):
    author = Author.query.filter_by(url = name).first_or_404()
    books = Book.query.filter_by(author_id = author.id)
    return render_template('author.html', books = books, author = author,
            title = author.name)



@app.route('/book/<title>/')
def book(title):
    book = Book.query.filter_by(url = title).first_or_404()
    pages = Page.query.filter(Page.book_id == book.id, 
            ).all()
    return render_template('book.html', book = book, pages = pages,
            title = book.title, author = book.author)



@app.route('/book/<title>/page<page_num>/')
def book_page(title, page_num):
    book = Book.query.filter_by(url = title).first_or_404()

    page = Page.query.filter(Page.page_num == page_num, 
            Page.book_id == book.id).first_or_404()

    next_page = Page.query.filter(Page.page_num == page.page_num+1, 
            Page.book_id == book.id).first()

    prev_page = Page.query.filter(Page.page_num == page.page_num-1, 
            Page.book_id == book.id).first()

    return render_template('book_page.html', book = book, author = book.author,
            title = book.title + f" p. {page.page_num}", 
            prev_page = prev_page, next_page = next_page, page = page)
