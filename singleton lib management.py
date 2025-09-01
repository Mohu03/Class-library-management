from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from model import Book
from database import engine, SessionLocal, Base
from factory import LibraryFactory

Base.metadata.create_all(bind=engine) 


class Library:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.session = SessionLocal()
            cls._instance.books = []  
        return cls._instance

    def add_book(self, title, copies):
        existing_book = self.session.query(Book).filter_by(title=title).first()
        if existing_book:
            existing_book.copies += copies
            existing_book.available_copies += copies
            print(f"Updated '{title}' with {copies} more copies.")
        else:
            book = LibraryFactory.create_book(title, copies)
            self.session.add(book)
            print(f"Added '{title}' with {copies} copies.")
        self.session.commit()



    def issue_book(self, title):
        book = self.session.query(Book).filter_by(title=title).first()
        if book:
            if book.available_copies > 0:
                book.available_copies -= 1
                self.session.commit()
                print(f"Issued '{title}' on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print(f"No copies of '{title}' available")
        else:
            print(f"Book '{title}' not found.")

    def return_book(self, title):
        book = self.session.query(Book).filter_by(title=title).first()
        if book:
            if book.available_copies < book.copies:
                book.available_copies += 1
                self.session.commit()
                print(f"Returned '{title}' on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print(f"All copies of '{title}' are already in library")
        else:
            print(f"Book '{title}' not found.")

    def check_availability(self, title):
        book = self.session.query(Book).filter_by(title=title).first()
        if book:
            if book.available_copies > 0:
                print(f"'{title}' is available.")
            else:
                print(f"'{title}' is currently unavailable.")
        else:
            print(f"'{title}' not found in library.")

    def display_books(self):
        print("\nLibrary Collection:")
        books = self.session.query(Book).all()
        for book in books:
            print(f"Title: {book.title}, Copies: {book.copies}, Available: {book.available_copies}")


if __name__ == "__main__":
    library1 = Library()
    library2 = Library()

    library1.add_book("Ikigai", 4)
    library1.add_book("Python", 5)
    library2.add_book("Python33", 3)

    library1.check_availability("Ikigai")
    library1.issue_book("Ikigai")
    library2.issue_book("Ikigai")
    library2.return_book("Ikigai")

    library1.display_books()
    library2.display_books()

