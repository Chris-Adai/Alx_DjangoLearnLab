# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    list_filter = ('publication_year',)  # Add filters for publication_year
    search_fields = ('title', 'author')  # Enable search by title and author