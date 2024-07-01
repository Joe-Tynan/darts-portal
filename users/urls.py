from django.urls import path

from .views import PlayerDetailView

app_name = 'players'
urlpatterns = [
    path('<slug:slug>/', PlayerDetailView.as_view(), name='player_detail'),
]