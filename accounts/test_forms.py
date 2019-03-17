from django.test import TestCase
from .forms import UserloginForm, UserRegistrationForm

# Create your tests here.

# methods need to start wiht test_


class TestUserloginForm(TestCase):
    """
    Test if the user login formm data is valid
    """

    def test_UserLoginForm_valid(self):
        form = UserloginForm(data={'username': 'user',
                                   'password': 'password'})
        self.assertTrue(form.is_valid())

    def test_for_missing_required_field(self):
        form = UserloginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])


class TestUserRegistrationForm(TestCase):
    """
    Test if the user registration formm data is valid
    """

    def test_UserRegistrationForm_valid(self):
        form = UserRegistrationForm(
            data={'username': 'user', 'password1': '12A@345a',
                  'password2': '12A@345a',
                  'email': 'someone@domain.ie'})
        self.assertTrue(form.is_valid())

    """
    Test if the user registration formm data is not valid
    """

    def test_UserRegistrationForm_invalid(self):
        form = UserRegistrationForm(
            data={'username': 'a', 'password1': 'b',
                  'password2': 'c',
                  'email': 'd'})
        self.assertFalse(form.is_valid())
