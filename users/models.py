import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=200, blank=True)

    # Yearly Functions
    def get_this_years_wins(self):
        return self.wins.all().filter(date__contains=datetime.date.today().year).count()
    
    def get_this_years_runner_ups(self):
        return self.runner_ups.all().filter(date__contains=datetime.date.today().year).count()
    
    def get_this_years_games_played(self):
        return self.games_played.filter(date__contains=datetime.date.today().year).count()
    
    # Monthly Functions
    def get_this_months_wins(self):
        return self.wins.all().filter(date__contains=datetime.date.today().month).count()
    
    def get_this_months_runner_ups(self):
        return self.runner_ups.all().filter(date__contains=datetime.date.today().month).count()
    
    def get_this_months_games_played(self):
        return self.games_played.filter(date__contains=datetime.date.today().month).count()
    
    # Weekly Functions
    def get_this_weeks_wins(self):
        return self.wins.all().filter(date__week=datetime.date.today().isocalendar()[1]).count()

    def get_this_weeks_runner_ups(self):
        return self.runner_ups.all().filter(date__week=datetime.date.today().isocalendar()[1]).count()

    def get_this_weeks_games_played(self):
        return self.games_played.filter(date__week=datetime.date.today().isocalendar()[1]).count()

    # Stats Functions
    def get_win_ratio(self):
        if( self.games_played.count() > 0  ):
            return round((self.wins.count() / self.games_played.count()), 2)
        else:
            return 'Not Played Yet'

    def get_last_win(self):
        if( self.wins.order_by('date').first() != None ):
            return self.wins.order_by('date').first()
        else:
            return 'NEVER!'

    def get_predicted_wins(self):
        return round((251 * self.get_win_ratio()), 2)

    def get_form(self):
        results = {}
        last_5_games = self.games_played.order_by('-date')[:5]

        for game in last_5_games:
            if game.winner.id == self.id:
                results[game.id] = 'win'
            elif game.runner_up.id == self.id:
                results[game.id] = 'runner-up'
            else:
                results[game.id] = 'loss'

        return results

    def get_longest_win_streak(self):
        pass

    def get_total_points(self):
        return self.wins.count()