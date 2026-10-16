class FavoriteBooks():
    def __init__(self):
        self.fav_book_list = []

    def add(self, book):
        self.fav_book_list.extend(book)

    def remove(self, book):
        self.fav_book_list.remove(book)

    def hasBook(self, book_id):
        for book in self.fav_book_list:
            if book_id == book.__book_id:
                return True

        return False