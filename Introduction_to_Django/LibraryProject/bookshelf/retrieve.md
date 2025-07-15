# retrieve.md

from bookshelf.models import Book

# Retrieve all book instances
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)

# Expected Output:
# 1984 George Orwell 1949

