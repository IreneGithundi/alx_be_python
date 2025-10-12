# library_system.py

class Book:
    def __init__(self, title, author):
        """Base class constructor to initialize common book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of a general book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook attributes and call the base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return string representation for an eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook attributes and call the base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return string representation for a print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize a library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library with their details."""
        for book in self.books:
            print(book)
