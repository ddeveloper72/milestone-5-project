from django.test import TestCase
from django.urls import resolve, reverse


class TestViews(TestCase):
    def test_get_home_page(self):
        """
        test for home page, by looking for server code 200
        """
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")