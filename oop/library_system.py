
class Book:
    def __init__(self, title, author):
        self.title = title      
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        Book.__init__(self, title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        Book.__init__(self, title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.book = book
        self.books.append(book)

    def list_books(self): 
        print(self.book)

 

