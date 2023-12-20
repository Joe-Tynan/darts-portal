from django.urls import path

from .views import RoadmapPageView

urlpatterns = [
    path('roadmap/', RoadmapPageView.as_view(), name='roadmap'),
]
