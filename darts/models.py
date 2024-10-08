import datetime

from django.db import models
from django.conf import settings

class Win(models.Model):
    date = models.DateField(auto_now_add=False, default=datetime.date.today)
    winner =  models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.CASCADE, related_name='wins')
    runner_up = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.CASCADE, related_name='runner_ups')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="games_played")

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='win_id_index'),
        ]

    def __str__(self):
        return str(self.date)
    
    def get_this_years_games_count(self):
        return Win.objects.filter(date__contains=datetime.date.today().year).count()
    
class Bet(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return str(self.description)
    
class Champion(models.Model):
    year = models.DateField()
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="championships")
    wins = models.IntegerField()

    def __str__(self):
        return str(self.year.year)