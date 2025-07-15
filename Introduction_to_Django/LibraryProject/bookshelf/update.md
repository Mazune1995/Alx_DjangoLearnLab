# update.md

from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
print(book.title)

# Expected Output:
# Nineteen Eighty-Four

