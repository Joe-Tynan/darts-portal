from django.urls import path

from .views import LapTimeTableView

urlpatterns = [
    path('', LapTimeTableView.as_view(), name='home'),
]