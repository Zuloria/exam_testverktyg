import sys
sys.path.insert(0, "../")
from book_store import *

def test_addBook():
    book_store = BookStore()

    author = "McPhillan"
    title = "How to tame a snail"

    book_id = book_store.addBook(author, title)
    book = book_store.findBook(book_id)

    assert book is not None
    assert book.__author == author
    assert book.__title == title

def test_toggleFavorite():
    book_store = BookStore()

    book_id_1 = book_store.addBook("Graham", "What if the sun is simply a firefly?")
    book_id_2 = book_store.addBook("Parvati", "The sun will never be a silly bug, period")

    book_store.toggleFavorite(book_id_2)

    assert book_store.fav_books.hasBook(book_id_2) == True
    assert book_store.fav_books.hasBook(book_id_1) == False

def test_findBook():
    book_store = BookStore()

    book_id = book_store.addBook("Ericsson", "To become a famous goose chaser: A true story")
    book = book_store.findBook(book_id)

    assert book is not None
    assert book.__book_id == book_id

