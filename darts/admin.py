from django.contrib import admin

from .models import Win, Bet

class WinAdmin(admin.ModelAdmin):
    list_display = ('date', 'winner', 'runner_up')

admin.site.register(Win, WinAdmin)
admin.site.register(Bet)