from django.test import TestCase
from django.urls import resolve, reverse


class TestViews(TestCase):
    def test_get_login_page(self):
        """
        test for login page, by looking for server code 200
        """
        page = self.client.get(reverse("login"))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_get_registration_page(self):
        """
        test for login page, by looking for server code 200
        """
        page = self.client.get(reverse("registration"))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")