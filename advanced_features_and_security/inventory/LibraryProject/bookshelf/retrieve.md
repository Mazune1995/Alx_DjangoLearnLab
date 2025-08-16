# retrieve.md

from bookshelf.models import Book

# Retrieve the specific book using Book.objects.get()
book = Book.objects.get(title="1984")

# Display all attributes
print(book.title)
print(book.author)
print(book.publication_year)

# Expected Output:
# 1984
# George Orwell
# 1949

