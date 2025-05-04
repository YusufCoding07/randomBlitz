from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileTests(TestCase):
    def test_profile_creation(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.assertTrue(hasattr(user, 'userprofile'))
