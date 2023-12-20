from django.urls import path

from .views import LeagueTableView, WinCreateView

urlpatterns = [
    path('', LeagueTableView.as_view(), name='home'),
    path('submit-win/', WinCreateView.as_view(), name='submit_win'),
]