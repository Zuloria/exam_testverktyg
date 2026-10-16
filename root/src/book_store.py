from book import Book
from fav_books import FavoriteBooks

class BookStore():
    def __init__(self):
        self.book_list = []
        self.id_counter = 0
        self.fav_books = FavoriteBooks()

    def addBook(self, author, title):
        book_id = self.id_counter
        self.id_counter += 1
        book = Book(book_id, author, title)
        self.book_list.extend(book)
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
            if book_id == book.__book_id:
                return book

            
            
