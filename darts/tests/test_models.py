import datetime

from django.test import TestCase

from users.models import CustomUser
from ..models import Win

class WinModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(username="testuser", password="test123")
        Win.objects.create(winner=user, runner_up=user)

    def test_wins_str_representation_function_shows_correct_information(self):
        date = datetime.date.today()
        win = Win.objects.get(id=1)
        
        self.assertEqual(str(win), str(date))
