from src.book_store import *
import pytest

@pytest.mark.integration
def test_toggleFavorite_add():
    fav_book = FavoriteBooks()
    book_store = BookStore(fav_book)

    title = "What if the sun is simply a firefly?"
    author = "Graham"

    book_id = book_store.addBook(title, author)

    book_store.toggleFavorite(book_id)

    assert fav_book.hasBook(book_id) is True

@pytest.mark.integration
def test_toggleFavorite_remove():
    fav_book = FavoriteBooks()
    book_store = BookStore(fav_book)

    title = "The sun will never be a silly bug, period"
    author = "Parvati"

    book_id = book_store.addBook(title, author)

    book_store.toggleFavorite(book_id)  # Add to favorites
    book_store.toggleFavorite(book_id)  # Remove from favorites

    assert fav_book.hasBook(book_id) is False
