import datetime

from django.test import TestCase
from django.urls import reverse, resolve

from .views import LeagueTableView, WinCreateView
from .models import Win

class HomePageTests(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('darts:home'))

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_home_page_html(self):
        self.assertContains(self.response, '<title>Darts Portal</title>')
        self.assertContains(self.response, 'Killer Darts Leaderboard')

    def test_home_page_url_resolves_to_correct_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, LeagueTableView.as_view().__name__)

class SubmitWinPageTests(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('darts:submit_win'))

    def test_submit_win_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_submit_win_page_template(self):
        self.assertTemplateUsed(self.response, 'create_win.html')

    def test_submit_win_page_html(self):
        self.assertContains(self.response, '<title>Darts Portal | Submit a Game</title>')
        self.assertContains(self.response, 'Submit a Game')

    def test_submit_win_page_url_resolves_to_correct_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, WinCreateView.as_view().__name__)


#class WinModelTest(TestCase):
    
    #def test_saving_and_retrieving_items(self):
        #first_item = Win()
        #first_item.date = datetime.date(1997, 10, 18)
        #first_item.winner = 1
        #first_item.save()

        #second_item = Win()
        #second_item.date = datetime.date(1997, 10, 19)
        #second_item.winner = 2
        #second_item.save()

        #saved_items = Win.objects.all()
        #self.assertEqual(saved_items.count(), 2)

        #first_saved_item = saved_items[0]
        #second_saved_item = saved_items[1]
        #self.assertEqual(first_saved_item.date, datetime.date(1997, 10, 18))
        #self.assertEqual(second_saved_item.date, datetime.date(1997, 10, 19))