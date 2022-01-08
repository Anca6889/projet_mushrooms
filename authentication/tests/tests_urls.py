"""This module will test all the urls"""

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from authentication import views


class UrlsTests(SimpleTestCase):
    """
    This class will test the urls using resolve and reverse modules
    Each method name describe exactly which url is tested.

    """

    def test_login_url_is_resolved(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, views.sign_in)

    def test_register_url_is_resolved(self):
        url = reverse("register")
        self.assertEquals(resolve(url).func, views.register)

    def test_account_url_is_resolved(self):
        url = reverse("account")
        self.assertEquals(resolve(url).func, views.account)

    def test_password_reset_url_is_resolved(self):
        url = reverse("password_reset")
        self.assertEquals(resolve(url).func, views.password_reset_request)

    def test_password_success_url_is_resolved(self):
        url = reverse("password_success")
        self.assertEquals(resolve(url).func, views.password_success)

    def test_sign_out_url_is_resolved(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func, views.sign_out)
