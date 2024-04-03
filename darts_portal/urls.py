from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('darts.urls')),
    path('', include('pages.urls')),
    path('karting/', include('karting.urls')),
    
    path('__debug__/', include("debug_toolbar.urls")),
]
