from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

url = reverse("home")


class HomeViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("Elijah", "elijah@gmail.com", "123")
        self.client.login(username="Elijah", password="123")
        self.response = self.client.get(reverse("home"))

    def test_template(self):
        self.assertTemplateUsed(self.response, "home.html")
