from django.contrib import admin

from .models import LapTime

class LapTimeAdmin(admin.ModelAdmin):
    list_display = ('time', 'driver')

admin.site.register(LapTime, LapTimeAdmin)