from django.urls import path

from . import views
from .views import LeagueTableView, WinCreateView, AllGamesView, AllResults, SubmitGameView

app_name = 'darts'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('all-games/', AllResults.as_view(), name='all_games'),
    path('submit-game/', SubmitGameView.as_view(), name='submit_game'),

    # Old URLs
    path('old/', LeagueTableView.as_view(), name='dashboard_old'),
    path('old/all-games/', AllGamesView.as_view(), name='all_games_old'),
    path('old/submit-win/', WinCreateView.as_view(), name='submit_win_old'),
]
