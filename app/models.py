from app import db


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100))
    author = db.Column(db.String(200))
    borrowed = db.Column(db.String(200))

    def __init__(self, book_name, author, borrowed):
        self.book_name = book_name
        self.author = author
        self.borrowed = borrowed

    def __str__(self):
        return f"<Book {self.book_name}>"