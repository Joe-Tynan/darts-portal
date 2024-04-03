from django.db import models
from django.conf import settings

class LapTime(models.Model):
    time = models.DurationField()
    driver =  models.ForeignKey(settings.AUTH_USER_MODEL, to_field='id', on_delete=models.CASCADE, related_name='lap_times')

    def __str__(self):
        return str(self.time)