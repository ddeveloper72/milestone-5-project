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

    def test_correct_message_for_missing_required_field(self):
        form = UserloginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])


class TestUserRegistrationForm(TestCase):
    """
    Test if the user registration formm data is valid
    """
    def test_UserRegistrationForm(self):
        form = UserRegistrationForm(
            data={'username': 'user', 'password1': 'password',
                  'password2': 'password',
                  'email': 'someone@domain.ie'})
        self.assertTrue(form.is_valid())
