from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        """
        Create test data before each test.
        """
        self.client = APIClient()

        # Create user for authenticated endpoints
        self.user = User.objects.create_user(
            username="tester",
            password="password123"
        )

        # Create an author
        self.author = Author.objects.create(name="John Writer")

        # Create books
        self.book1 = Book.objects.create(
            title="Book One",
            publication_year=2020,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Another Story",
            publication_year=2021,
            author=self.author
        )

        # URLs
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.id])

    # -----------------------------
    #     READ TESTS
    # -----------------------------
    def test_list_books(self):
        """
        Test retrieving list of all books (public access).
        """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """
        Test retrieving a single book by ID.
        """
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book One")

    # -----------------------------
    #     CREATE TEST
    # -----------------------------
    def test_create_book_requires_auth(self):
        """
        Test creating a book without auth (should fail).
        """
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """
        Test creating a book with authentication.
        """
        self.client.login(username="tester", password="password123")

        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }

        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    # -----------------------------
    #     UPDATE TEST
    # -----------------------------
    def test_update_book(self):
        """
        Test updating book details.
        """
        self.client.login(username="tester", password="password123")

        data = {"title": "Updated Title"}

        response = self.client.patch(self.detail_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    # -----------------------------
    #     DELETE TEST
    # -----------------------------
    def test_delete_book(self):
        """
        Ensure authenticated user can delete.
        """
        self.client.login(username="tester", password="password123")

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # -----------------------------
    #     FILTERING TESTS
    # -----------------------------
    def test_filter_by_title(self):
        response = self.client.get(self.list_url + "?title=Book One")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    # -----------------------------
    #     SEARCH TESTS
    # -----------------------------
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Another")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Another Story")

    # -----------------------------
    #     ORDERING TESTS
    # -----------------------------
    def test_order_books_by_year(self):
        response = self.client.get(self.list_url + "?ordering=-publication_year")

        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
    def test_order_books_by_title(self):
        response = self.client.get(self.list_url + "?ordering=title")

        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))
        