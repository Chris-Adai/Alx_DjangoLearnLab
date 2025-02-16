from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# No output is displayed if the operation is successful.
# Verify the deletion by retrieving all books:
Book.objects.all()
# Output: <QuerySet []>


