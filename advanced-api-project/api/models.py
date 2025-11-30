from django.db import models

# Author model stores information about writers.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name of the author

    def __str__(self):
        return self.name


# Book model stores books written by authors.
# It has a ForeignKey creating a one-to-many relationship:
# One Author → many Books
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(
        Author,
        related_name='books',  # Allows author.books to access all books
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

# Create your models here.
