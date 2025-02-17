import datetime
from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from darts.models import Win

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=200, blank=True)
    plays_darts = models.BooleanField(default=True)

    class Meta:
        ordering = ['first_name', 'last_name']
        indexes = [
            models.Index(fields=['id'], name='user_id_index'),
        ]

    # Admin Functions
    def display_user_wins(self):
        return self.wins.count()
    
    display_user_wins.short_description = 'Wins'

    # General Functions
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def get_absolute_url(self):
        return reverse("players:player_detail", args=[str(self.id)])

    # Yearly Functions
    def get_this_years_wins(self):
        return self.wins.all().filter(date__contains=datetime.date.today().year).count()
    
    def get_this_years_runner_ups(self):
        return self.runner_ups.all().filter(date__contains=datetime.date.today().year).count()

    def get_this_years_losses(self):
        return self.games_played.filter(date__contains=datetime.date.today().year).exclude(winner__id=self.id).count()
    
    def get_this_years_games_played(self):
        return self.games_played.filter(date__contains=datetime.date.today().year).count()
    
    def get_this_years_games_played_percentage(self):
        games_played_by_user = self.games_played.filter(date__contains=datetime.date.today().year).count()
        total_games_played = Win.objects.filter(date__contains=datetime.date.today().year).count()

        if (total_games_played > 0):
            return round(((games_played_by_user / total_games_played) * 100), 1)
        else:
            return 0
    
    # Monthly Functions
    def get_this_months_wins(self):
        return self.wins.all().filter(date__month=datetime.date.today().month).filter(date__contains=datetime.date.today().year).count()
    
    def get_this_months_runner_ups(self):
        return self.runner_ups.all().filter(date__month=datetime.date.today().month).filter(date__contains=datetime.date.today().year).count()
    
    def get_this_months_games_played(self):
        return self.games_played.filter(date__month=datetime.date.today().month).filter(date__contains=datetime.date.today().year).count()
    
    # Weekly Functions
    def get_this_weeks_wins(self):
        return self.wins.all().filter(date__week=datetime.date.today().isocalendar()[1]).filter(date__contains=datetime.date.today().year).count()

    def get_this_weeks_runner_ups(self):
        return self.runner_ups.all().filter(date__week=datetime.date.today().isocalendar()[1]).filter(date__contains=datetime.date.today().year).count()

    def get_this_weeks_games_played(self):
        return self.games_played.filter(date__week=datetime.date.today().isocalendar()[1]).filter(date__contains=datetime.date.today().year).count()

    # Stats Functions
    def get_win_ratio(self):
        if( self.games_played.filter(date__contains=datetime.date.today().year).count() > 0  ):
            return round((self.wins.filter(date__contains=datetime.date.today().year).count() / self.games_played.filter(date__contains=datetime.date.today().year).count() * 100), 1)
        else:
            return 0

    def get_last_win(self):
        today = datetime.date.today()
        yesterday = datetime.date.today() - timedelta(1)
        last_win = self.wins.order_by('-date').first()

        if( last_win != None ):
            if( last_win.date == today ):
                return 'Today'
            elif( last_win.date == yesterday ):
                return 'Yesterday'
            else:
                return last_win.date.strftime('%a %d %b %Y')
        else:
            return 'NEVER!'
        
    def get_last_game_played(self):
        today = datetime.date.today()
        yesterday = datetime.date.today() - timedelta(1)
        last_game_played = self.games_played.order_by('-date').first()

        if( last_game_played != None ):
            if( last_game_played.date == today ):
                return 'Today'
            elif( last_game_played.date == yesterday ):
                return 'Yesterday'
            else:
                return last_game_played.date.strftime('%a %d %b %Y')
        else:
            return 'NEVER!'

    def get_predicted_wins(self):
        last_game_played = self.games_played.filter(date__contains=datetime.date.today().year).order_by('-date').first()

        if( last_game_played != None ):
            return round((251 * self.get_win_ratio() / 100), 2)
        else:
            return 0

    def get_form(self):
        results = {}
        last_10_games = self.games_played.filter(date__contains=datetime.date.today().year).order_by('-date')[:10]

        for game in last_10_games:
            if game.winner.id == self.id:
                results[game.id] = 'win'
            elif game.runner_up.id == self.id:
                results[game.id] = 'runner-up'
            else:
                results[game.id] = 'loss'

        return results
    
    def get_form_score(self):
        form = 0
        last_10_games = self.games_played.filter(date__contains=datetime.date.today().year).order_by('-date')[:10]

        for game in last_10_games:
            if game.winner.id == self.id:
                form += 1
            elif game.runner_up.id == self.id:
                form += 0.5

        return form
    
    def get_form_emoji(self):
        form = float(self.get_form_score())
        emoji = ''

        if form >= 10:
            emoji = '👑'
        elif form >= 9:
            emoji = '💎'
        elif form >= 7.5:
            emoji = '🦄'
        elif form >= 6:
            emoji = '🤯'
        elif form >= 4.5:
            emoji = '🔥'
        elif form >= 3:
            emoji = '🤌'
        elif form >= 1.5:
            emoji = '😐'
        elif form >= 0.5:
            emoji = '🐌'
        else:
            emoji = '💩'

        return emoji

    def get_longest_win_streak(self):
        pass

    def get_total_points(self):
        return self.wins.count()