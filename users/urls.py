from django.urls import path

from .views import PlayerDetailView
from .views import all_players_api_view

app_name = 'players'
urlpatterns = [
    path('<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),
    path('api/players/', all_players_api_view, name='api_all_players'),
]