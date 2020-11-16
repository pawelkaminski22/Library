from app import app, db
from app.models import Books


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Books": Books,
        "Borrowed": Borrow
    }
