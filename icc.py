from app import app, db
from app.models import User, Book, Page, Author

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Book': Book, 'Author': Author, 'Page':
            Page}
# This is another test
