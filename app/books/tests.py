import json
from urllib.parse import urljoin
#
from rest_framework import status
from rest_framework.test import APITestCase
from books import models, serializers


class BookTest(APITestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1/api/"


    def test_add_authors(self):
        data = {
            "first_name": "Isaac",
            "last_name": "Asimov",
            "email": "asimov@mail.com"
        }

        response = self.client.post(urljoin(self.base_url, "add-author/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Author.objects.count(), 1)
        self.assertEqual(models.Author.objects.get(id=1).last_name, "Asimov")
        self.assertEqual(models.Author.objects.get(id=1).birthday, None)

        data = {
            "first_name": "Ray",
            "last_name": "Bradbury",
            "birthday": "1920-8-22",
            "email": "bradbury@mail.com"
        }

        response = self.client.post(urljoin(self.base_url, "add-author/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Author.objects.count(), 2)
        self.assertEqual(models.Author.objects.get(id=2).last_name, "Bradbury")

        data = {
            "first_name": "Charles",
            "last_name": "Dickens",
            "email": "dickens"  # Note: invalid mail
        }

        response = self.client.post(urljoin(self.base_url, "add-author/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)        


    def test_add_publishers(self):
        data = {
            "name": "HarperCollins Publishers",
            "address": "London, United Kingdom",
            "phone_number": "+41524204242"
        }

        response = self.client.post(urljoin(self.base_url, "add-publisher/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = {
            "name": "HarperCollins Publishers",  # uniqueness constraint should cause failure
        }

        response = self.client.post(urljoin(self.base_url, "add-publisher/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {
            "name": "publisher-1",
            "phone_number": "lorem ipsum"  # Note: invalid phone number
        }

        response = self.client.post(urljoin(self.base_url, "add-publisher/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_manage_books(self):

        # Add an author and a publisher

        data = {
            "first_name": "Isaac",
            "last_name": "Asimov",
            "email": "asimov@mail.com"
        }

        self.client.post(urljoin(self.base_url, "add-author/"), data, format="json")

        data = {
            "name": "HarperCollins Publishers",
            "address": "London, United Kingdom",
            "phone_number": "+41524204242"
        }

        self.client.post(urljoin(self.base_url, "add-publisher/"), data, format="json")

        # Add a book (valid, all fields)
        data = {
            "title": "test-book-1",
            "description": "lorem ipsum",
            "isbn": "9780393059748",
            "pub_date": "2020-12-10",
            "author": 1,
            "publisher": 1
        }

        response = self.client.post(urljoin(self.base_url, "add-book/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["visibility"], True)

        data = {
            "title": "test-book-2",
            "description": "lorem ipsum",
            "isbn": "9780393059748",  # uniqueness constraint
            "pub_date": "2020-12-10",
            "author": 1,
            "publisher": 1
        }

        response = self.client.post(urljoin(self.base_url, "add-book/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Add another book (valid, required fields only)
        data = {
            "title": "test-book-3",
            "isbn": "9781472103536",
            "author": 1
        }

        response = self.client.post(urljoin(self.base_url, "add-book/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            "title": "test-book-3",
            "isbn": "9781472103536",
            "author": 1,
            "description": None,
            "pub_date": None,
            "publisher": None,
            "visibility": True
        })

        # Update book (id=2)
        data = {
            "description": "lorem ipsum",
            "visibility": False,
        }

        response = self.client.patch(urljoin(self.base_url, "upd-book/2/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.json(), {
            "title": "test-book-3",
            "isbn": "9781472103536",
            "author": 1,
            "description": "lorem ipsum",
            "pub_date": None,
            "publisher": None,
            "visibility": False
        })
