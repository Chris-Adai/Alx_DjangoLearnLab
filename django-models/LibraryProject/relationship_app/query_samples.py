# import os
# import django

# # # Set up Django environment
# # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
# # django.setup()

# from relationship_app.models import Author, Book, Library, Librarian

# # Query all books by a specific author
# def get_books_by_author(author_name):
#     author = Author.objects.filter(name=author_name).first()
#     if author:
#         return author.books.all()
#     return []

# # List all books in a library
# def get_books_in_library(library_name):
#     library = Library.objects.filter(name=library_name).first()
#     if library:
#         return library.books.all()
#     return []

# # Retrieve the librarian for a library
# def get_librarian_for_library(library_name):
#     library = Library.objects.filter(name=library_name).first()
#     if library:
#         return library.librarian
#     return None

# # Example usage
# if __name__ == "__main__":
#     print(get_books_by_author("J.K. Rowling"))
#     print(get_books_in_library("Central Library"))
#     print(get_librarian_for_library("Central Library"))



import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Use get() instead of filter().first()
        return author.books.all()
    except Author.DoesNotExist:
        return []

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Use get() instead of filter().first()
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Use get() instead of filter().first()
        return library.librarian
    except Library.DoesNotExist:
        return None

# Example usage
if __name__ == "__main__":
    print(get_books_by_author("J.K. Rowling"))
    print(get_books_in_library("Central Library"))
    print(get_librarian_for_library("Central Library"))
