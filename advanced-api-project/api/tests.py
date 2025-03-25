from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book
import json

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="Test Author")
        self.book_data = {
            'title': 'Test Book',
            'publication_year': 2020,
            'author': self.author.id
        }
        self.book = Book.objects.create(
            title='Existing Book',
            publication_year=2019,
            author=self.author
        )

    def test_create_book(self):
        response = self.client.post(
            reverse('book-list'),
            data=json.dumps(self.book_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book_list(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_book_detail(self):
        response = self.client.get(
            reverse('book-detail', kwargs={'pk': self.book.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Existing Book')

    def test_update_book(self):
        updated_data = {
            'title': 'Updated Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.put(
            reverse('book-detail', kwargs={'pk': self.book.id}),
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(
            reverse('book-detail', kwargs={'pk': self.book.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        # Create another book for filtering
        Book.objects.create(
            title='Another Book',
            publication_year=2018,
            author=self.author
        )
        response = self.client.get(
            reverse('book-list') + '?title=Existing'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Existing Book')

    def test_search_books(self):
        response = self.client.get(
            reverse('book-list') + '?search=Existing'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Existing Book')

    def test_order_books(self):
        Book.objects.create(
            title='A Book',
            publication_year=2018,
            author=self.author
        )
        response = self.client.get(
            reverse('book-list') + '?ordering=title'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'A Book')
        self.assertEqual(response.data[1]['title'], 'Existing Book')