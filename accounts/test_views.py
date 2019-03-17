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

    def test_get_profile_page(self):
        """
        test for user_profile page, by first esding reqeust to
        server and expecting 302 response.  Then sending test login
        credentials
        """
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 302)
        self.client.login(username="test", password="test")
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 302)