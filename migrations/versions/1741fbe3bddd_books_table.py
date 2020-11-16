"""books table

Revision ID: 1741fbe3bddd
Revises: 
Create Date: 2020-11-13 22:38:26.894607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1741fbe3bddd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_name', sa.String(length=100), nullable=True),
    sa.Column('author', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_author'), 'books', ['author'], unique=True)
    op.create_index(op.f('ix_books_book_name'), 'books', ['book_name'], unique=True)
    op.create_table('borrow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('borrowed', sa.Text(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrow')
    op.drop_index(op.f('ix_books_book_name'), table_name='books')
    op.drop_index(op.f('ix_books_author'), table_name='books')
    op.drop_table('books')
    # ### end Alembic commands ###
