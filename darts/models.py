import datetime

from django.db import models
from django.conf import settings

class Win(models.Model):
    date = models.DateField(auto_now_add=False, default=datetime.date.today)
    winner =  models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.CASCADE, related_name='wins')
    runner_up = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.CASCADE, related_name='runner_ups')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="games_played")

    def __str__(self):
        return str(self.date)