```python
from bookshelf.models import Book

# Retrieve all book records
books = Book.objects.all()
print(books)

# Delete the specific book (for example, "Nineteen Eighty-Four")
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)
