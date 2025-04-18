from django.db import models

# Create your models here.
# from django.db import models

class Author(models.Model):
    """Represents an author who writes books"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Represents a book written by an author"""
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title