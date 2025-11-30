from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import (
    BookListView, BookDetailView,
    BookCreateView, BookUpdateView, BookDeleteView
)

"""
URL routing for Book API endpoints.

Endpoints:
- /books/            -> List all books (GET)
- /books/<pk>/       -> Retrieve single book (GET)
- /books/create/     -> Create new book (POST)
- /books/<pk>/update/ -> Update book (PUT/PATCH)
- /books/<pk>/delete/ -> Delete book (DELETE)
"""
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
urlpatterns = router.urls
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
] 