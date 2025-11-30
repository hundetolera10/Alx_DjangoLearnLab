# Book API - Generic Views Setup

## Endpoints
- GET /api/books/ - List all books
- GET /api/books/<pk>/ - Retrieve one book
- POST /api/books/create/ - Create new book
- PUT/PATCH /api/books/<pk>/update/ - Update book
- DELETE /api/books/<pk>/delete/ - Delete book

## Permissions
- List & Detail: Public
- Create, Update, Delete: Only authenticated users

## View Types
Each view uses DRF generic views:
- ListAPIView
- RetrieveAPIView
- CreateAPIView
- UpdateAPIView
- DestroyAPIView
### Filtering
Use query parameters like:
- ?title__icontains=python
- ?author__icontains=john
- ?publication_year=2020

### Searching
- ?search=python
- ?search=rowling

### Ordering
- ?ordering=title
- ?ordering=-publication_year
## Running Tests

To execute the full test suite:

    python manage.py test api

### Tests Included:
- CRUD operations for Book API
- Permission and authentication checks
- Filtering (title, author, publication_year)
- Searching (title, author name)
- Ordering (title, publication_year)
