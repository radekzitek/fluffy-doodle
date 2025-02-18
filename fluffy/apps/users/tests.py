from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
import json


class UserTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_data = {
            "username": "testuser",
            "password": "testpassword123",
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_register_user(self):
        response = self.client.post(
            reverse("register_user"),
            data=json.dumps(self.user_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())
        self.assertIn("username", response.json())
        self.assertIn("email", response.json())

    def test_get_user_profile(self):
        self.client.login(
            username=self.user_data["username"], password=self.user_data["password"]
        )
        response = self.client.get(reverse("get_user_profile"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("username", response.json())
        self.assertIn("email", response.json())

    def test_update_user_profile(self):
        self.client.login(
            username=self.user_data["username"], password=self.user_data["password"]
        )
        updated_data = {"first_name": "Updated", "last_name": "User"}
        response = self.client.patch(
            reverse("update_user_profile"),
            data=json.dumps(updated_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["first_name"], "Updated")
        self.assertEqual(response.json()["last_name"], "User")
