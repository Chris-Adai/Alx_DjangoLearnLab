### Create Operation

#### Command:
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()


# No output is displayed if the operation is successful.
# You can verify the creation by retrieving the book:
# Book.objects.all()
# Output:
<QuerySet [<Book: 1984 by George Orwell (1949)>]>



