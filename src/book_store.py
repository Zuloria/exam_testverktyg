from src.book import Book
from src.fav_books import FavoriteBooks

class BookStore():
    def __init__(self, fav_books=FavoriteBooks()):
        self.book_list = []
        self.id_counter = 0
        self.fav_books = fav_books

    def addBook(self, title, author):
        book_id = self.id_counter
        self.id_counter += 1
        book = Book(book_id, title, author)
        self.book_list.append(book)
        return book_id

    def toggleFavorite(self, book_id):
        book = self.findBook(book_id)
        if book == None:
            return

        if self.fav_books.hasBook(book_id):
            self.fav_books.remove(book)
        else:
            self.fav_books.add(book)

    def findBook(self, book_id):
        for book in self.book_list:
            if book_id == book.book_id:
                return book

            
            
