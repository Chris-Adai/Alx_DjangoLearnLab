# # api/urls.py
# from django.urls import path
# from .views import BookList

# urlpatterns = [
#     path('books/', BookList.as_view(), name='book-list'),
# ]

###########################################333

# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from .views import (
    BookListCreateView, BookDetailView,
    AuthorListCreateView, AuthorDetailView
)

# Initialize router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Simple ListAPIView
    path('books/', BookList.as_view(), name='book-list'),

    # ViewSet CRUD routes
    path('', include(router.urls)),
]

#

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]