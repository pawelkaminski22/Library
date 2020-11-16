from flask import request, render_template, redirect, url_for, flash
from app import app, forms, db, models


@app.route('/')
def index():
    Books = models.Books
    books = Books.query.all()
    return render_template('new.html', books=books)


@app.route('/post_book', methods=['POST'])
def post_book():
    Books = models.Books
    book = Books(request.form['book_name'], request.form['author'], request.form['borrowed'])
    db.session.add(book)
    db.session.commit()
    flash(f'Book added!')
    return redirect(url_for('index'))


@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    Books = models.Books
    BookForm = forms.BookForm
    book = Books.query.get(book_id)
    book_values = {'book_name': book.book_name, 'author': book.author, 'borrowed': book.borrowed}
    form = BookForm(data=book_values)

    if request.method == "POST":
        if 'Update' in request.form:
            book_name = request.form['book_name']
            author = request.form['author']
            borrowed = request.form['borrowed']
            book = Books.query.get(book_id)
            book.book_name = book_name
            book.author = author
            book.borrowed = borrowed
            db.session.commit()

        elif 'Delete' in request.form:
            book = Books.query.get(book_id)
            db.session.delete(book)
            db.session.commit()
        return redirect(url_for("index"))
    return render_template("details.html", form=form, book_id=book_id)
