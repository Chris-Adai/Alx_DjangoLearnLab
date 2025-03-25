# from django.urls import path
# from .views import (
#     BookListCreateView, BookDetailView,
#     AuthorListCreateView, AuthorDetailView
# )

# urlpatterns = [
#     path('books/', BookListCreateView.as_view(), name='book-list'),
#     path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
#     path('authors/', AuthorListCreateView.as_view(), name='author-list'),
#     path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
# ]

#######################3

from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # List all books or create a new one
    path('books/', BookListView.as_view(), name='book-list'),
    
    # Create a new book (separate endpoint for clarity)
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    
    # Retrieve, update, or delete a specific book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]