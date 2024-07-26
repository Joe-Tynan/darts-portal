from django.urls import path

from . import views
from .views import LeagueTableView, WinCreateView, AllGamesView, AllBetsView

app_name = 'darts'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('old/', LeagueTableView.as_view(), name='dashboard_old'),

    path('submit-win/', WinCreateView.as_view(), name='submit_win_old'),

    path('all-games/', AllGamesView.as_view(), name='all_games_old'),
    path('bets/', AllBetsView.as_view(), name='bets_old'),
]