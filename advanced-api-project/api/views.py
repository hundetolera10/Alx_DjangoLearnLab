from rest_framework import generics
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

 
"""
BOOK CRUD VIEWS USING DRF GENERIC VIEWS

We are implementing:
- ListView      -> Retrieve all books
- DetailView    -> Retrieve one book by ID
- CreateView    -> Add a new book
- UpdateView    -> Modify an existing book
- DeleteView    -> Remove a book

Permissions:
- Anyone can READ (List + Detail)
- Only authenticated users can CREATE, UPDATE, DELETE
"""

# -----------------------------
# 1. LIST ALL BOOKS (GET only)
# -----------------------------
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Filtering
    filterset_fields = ['title','author', 'publication_year']   
    # Searching
    search_fields = ['title', 'author']
    # Ordering
    ordering_fields = ['title', 'publication_year']

class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    This endpoint is READ-ONLY and open to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filtering
    filterset_fields = ['title','author', 'publication_year']

    # Searching
    search_fields = ['title', 'author']

    # Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

# -----------------------------
# 2. RETRIEVE SINGLE BOOK (GET)
# -----------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns a single book using its primary key.
    This endpoint is also READ-ONLY.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------
# 3. CREATE A BOOK (POST)
# -----------------------------
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new Book.
    Automatically runs serializer validations (e.g., publication_year not future).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom behavior during creation.
        Hooks into DRF lifecycle.
        """
        serializer.save()  # You could add logs, ownership, etc.


# -----------------------------
# 4. UPDATE A BOOK (PUT/PATCH)
# -----------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update an existing Book.
    PATCH = partial update
    PUT   = full update
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom behavior during update.
        """
        serializer.save()


# -----------------------------
# 5. DELETE A BOOK (DELETE)
# -----------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        """
        Custom delete hook.
        """
        instance.delete()

# Create your views here.
