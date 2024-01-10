from django.urls import path

from .views import LeagueTableView, WinCreateView, AllGamesView, AllBetsView

urlpatterns = [
    path('', LeagueTableView.as_view(), name='home'),
    path('submit-win/', WinCreateView.as_view(), name='submit_win'),
    path('all-games/', AllGamesView.as_view(), name='all_games'),
    path('bets/', AllBetsView.as_view(), name='bets'),
]