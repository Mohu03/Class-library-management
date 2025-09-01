from model import Book

class LibraryFactory:
    @staticmethod
    def create_book(title, copies):
        return Book(title=title, copies=copies, available_copies=copies)
