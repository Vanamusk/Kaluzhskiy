
class Library:
    def __init__(self, name, books = []):
        self.name = name
        self.books = books
        self.n_books = len(books)
    
    def __add__(self, book):
        addedbooks = self.books + [book]
        return Library(name = self.name, books = addedbooks)
    
    def __iadd__(self, book):
        addedbooks = self.books + [book]
        return Library(name = self.name, books = addedbooks)
    
    def __lt__(self, library): #x < y
        return self.n_books < library.n_books
        
    def __le__(self, library): #x <= y
        return self.n_books <= library.n_books
    
    def __eq__(self, library): #x == y
        return self.n_books == library.n_books
    
    def __ne__(self, library): #x != y
        return self.n_books != library.n_books
    
    def __gt__(self, library): #x > y
        return self.n_books > library.n_books
    
    def __ge__(self, library): #x >= y
        return self.n_books >= library.n_books
    
    def __str__(self):
        return f"{self.name} (число книг: {self.n_books})"
    
    def __repr__(self):
        return f"Library(name = \"{self.name}\")"
    
    
class Book:
    def __init__(self,name,author,year):
        self.name = name
        self.author = author
        self.year = year

