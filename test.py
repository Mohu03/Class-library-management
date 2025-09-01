from datetime import datetime

class Book:
    def __init__(self, title, total_copies):
        self.title = title
        self.total_copies = total_copies
        self.available_copies = total_copies

    def issue(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

class Library:
    def __init__(self):
        self.books = {}  

    def add_book(self, title, copies):
        if title in self.books:
            self.books[title].total_copies += copies
            self.books[title].available_copies += copies
        else:
            self.books[title] = Book(title, copies)
        print(f"Book '{title}' added/updated successfully.")

    def issue_book(self, title):
        if title in self.books and self.books[title].issue():
            print(f"Book '{title}' issued successfully.")
        else:
            print(f"Book '{title}' is not available.")

    def return_book(self, title):
        if title in self.books and self.books[title].return_book():
            print(f"Book '{title}' returned successfully.")
        else:
            print(f"Book '{title}' was not issued or doesn't exist.")

    def check_availability(self, title):
        if title in self.books:
            if self.books[title].available_copies > 0:
                print(f"'{title}' is available ({self.books[title].available_copies} copies left).")
            else:
                print(f"'{title}' is currently unavailable.")
        else:
            print(f"'{title}' not found in the library.")

    def display_books(self):
        print("\nLibrary Collection:")
        if not self.books:
            print("No books in library.")
        for book in self.books.values():
            print(f"Title: {book.title}, Total Copies: {book.total_copies}, Available: {book.available_copies}")


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
