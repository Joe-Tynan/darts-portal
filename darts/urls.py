from django.urls import path

from . import views
from .views import LeagueTableView, WinCreateView, AllGamesView, AllBetsView

app_name = 'darts'
urlpatterns = [
    path('', LeagueTableView.as_view(), name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit-win/', WinCreateView.as_view(), name='submit_win'),
    path('all-games/', AllGamesView.as_view(), name='all_games'),
    path('bets/', AllBetsView.as_view(), name='bets'),
]