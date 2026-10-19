from src.book_store import *
import pytest

@pytest.mark.unit
def test_addBook():
    book_store = BookStore()

    title = "How to tame a snail"
    author = "McPhillan"
   
    book_id = book_store.addBook(title, author)
    book = book_store.findBook(book_id)

    assert book is not None
    assert book.title == title
    assert book.author == author

@pytest.mark.unit
def test_toggleFavorite_add(mock_fb):
    book_store = BookStore(mock_fb)

    title = "What if the sun is simply a firefly?"
    author = "Graham"

    mock_fb.hasBook.return_value = False

    book_id = book_store.addBook(title, author)

    book_store.toggleFavorite(book_id)

    mock_fb.add.assert_called_once_with(book_store.findBook(book_id))

@pytest.mark.unit
def test_toggleFavorite_remove(mock_fb):
    book_store = BookStore(mock_fb)

    title = "The sun will never be a silly bug, period"
    author = "Parvati"

    mock_fb.hasBook.return_value = False

    book_id = book_store.addBook(title, author)

    book_store.toggleFavorite(book_id)

    mock_fb.add.assert_called_once_with(book_store.findBook(book_id))

    mock_fb.hasBook.return_value = True

    book_store.toggleFavorite(book_id)

    mock_fb.remove.assert_called_once_with(book_store.findBook(book_id))

@pytest.mark.unit
def test_findBook():
    book_store = BookStore()

    title = "To become a famous goose chaser: A true story"
    author = "Ericsson"

    book_id = book_store.addBook(title, author)
    book = book_store.findBook(book_id)

    assert book is not None
    assert book.book_id == book_id

