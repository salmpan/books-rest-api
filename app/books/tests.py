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
            "phone": "+41524204242"
        }

        response = self.client.post(urljoin(self.base_url, "add-publisher/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = {
            "name": "HarperCollins Publishers",  # uniqueness constraint should cause failure
        }

        response = self.client.post(urljoin(self.base_url, "add-publisher/"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_manage_book(self):
        # TODO
        pass


    def test_list_books(self):
        # TODO
        pass
