from src.fav_books import *
from src.book import *
import pytest

@pytest.mark.unit
def test_add():
    fav_book = FavoriteBooks()

    book_id = 5
    title = "Cats will one day rule the Earth, and we will be their slaves"
    author = "Morrison"

    book = Book(book_id, title, author)
    fav_book.add(book)

    assert fav_book.hasBook(book_id) is True

@pytest.mark.unit
def test_remove():
    fav_book = FavoriteBooks()

    book_id = 7
    title = "The neverending story of capitalism: A diary of a janitor"
    author = "Persson"

    book = Book(book_id, title, author)
    fav_book.add(book)

    fav_book.remove(book)

    assert fav_book.hasBook(book_id) is False
    
@pytest.mark.unit
def test_hasBook():
    fav_book = FavoriteBooks()

    book_id = 9

    assert fav_book.hasBook(book_id) is False
    