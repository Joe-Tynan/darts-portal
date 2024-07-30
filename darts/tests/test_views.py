from django.test import TestCase
from django.urls import reverse

from ..models import Win

class WinViewTests(TestCase):

    def test_dashboard_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_url_accessible_by_name(self):
        response = self.client.get(reverse('darts:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_uses_correct_template(self):
        response = self.client.get(reverse('darts:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'darts/dashboard.html')