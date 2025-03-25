# # from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics
# from .models import Book, Author
# from .serializers import BookSerializer, AuthorSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend

# class BookListCreateView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['title', 'author__name', 'publication_year']
#     search_fields = ['title', 'author__name']
#     ordering_fields = ['title', 'publication_year']
#     ordering = ['title']  # Default ordering
    
# class BookListCreateView(generics.ListCreateAPIView):
#     """Handles listing and creating books"""
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """Handles retrieving, updating and deleting a single book"""
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class AuthorListCreateView(generics.ListCreateAPIView):
#     """Handles listing and creating authors"""
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """Handles retrieving, updating and deleting a single author"""
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

#####################

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status

class BookListView(generics.ListAPIView):
    """
    View to list all books (GET request).
    No authentication required for reading.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view

    def get_queryset(self):
            """
            Add filtering capabilities to the list view.
            Example: /books/?author=Stephen+King
            """
            queryset = Book.objects.all()
            author = self.request.query_params.get('author', None)
            if author is not None:
                queryset = queryset.filter(author__icontains=author)
            return queryset

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by ID (GET request).
    No authentication required for reading.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book (POST request).
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Optionally add custom logic during creation.
        For example, automatically set the book's owner to the current user.
        """
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Custom response format for creation.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'status': 'success',
            'message': 'Book created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)
    
class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book (PUT/PATCH requests).
    Requires authentication and ownership or admin status.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


    def get_queryset(self):
        """
        For non-admin users, only return books they own.
        Admins can edit any book.
        """
        user = self.request.user
        if user.is_staff:
            return Book.objects.all()
        return Book.objects.filter(owner=user)

class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book (DELETE request).
    Requires authentication and ownership or admin status.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


    def get_queryset(self):
        """
        For non-admin users, only return books they own.
        Admins can delete any book.
        """
        user = self.request.user
        if user.is_staff:
            return Book.objects.all()
        return Book.objects.filter(owner=user)
    
#

class BookListView(generics.ListAPIView):
    # ... existing code ...
    
    def get_queryset(self):
        """
        Add filtering capabilities to the list view.
        Example: /books/?author=Stephen+King
        """
        queryset = Book.objects.all()
        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author__icontains=author)
        return queryset

class BookCreateView(generics.CreateAPIView):
    # ... existing code ...
    
    def create(self, request, *args, **kwargs):
        """
        Custom response format for creation.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'status': 'success',
            'message': 'Book created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)