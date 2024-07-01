from django.urls import path

#from .views import RoadmapPageView
from .views import WebpackPageView

urlpatterns = [
    #path('roadmap/', RoadmapPageView.as_view(), name='roadmap'),
    path('webpack/', WebpackPageView.as_view(), name='roadmap'),
]
