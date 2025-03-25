from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Author(models.Model):
    """Represents an author who writes books"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name