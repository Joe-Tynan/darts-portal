from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('darts.urls', namespace='darts')),
    path('players/', include('users.urls')),

    path('__debug__/', include("debug_toolbar.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
