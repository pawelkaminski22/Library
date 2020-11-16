from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email


class BookForm(FlaskForm):
    book_name = StringField('Book name', validators=[DataRequired()])
    author = TextAreaField('Author')
    borrowed = BooleanField('Borrowed')
