class Book:
    def __init__(self, title, author): 
        self.title = title
        self.author = author
        self.is_checked_out = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)

    def list_available_books(self):
        # Fixed: Return only available books and fixed syntax error
        return [book for book in self.books if not book.is_checked_out]
    
    def check_out_book(self, title):
        # Fixed: Find existing book by title, don't create new one
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                return True
        return False  # Book not found or already checked out

    def return_book(self, title): 
        # Fixed: Find existing book by title, don't create new one
        for book in self.books:
            if book.title == title and book.is_checked_out:
                book.is_checked_out = False
                return True
        return False  # Book not found or not checked out