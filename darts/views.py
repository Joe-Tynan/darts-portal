import datetime

from django.views.generic import ListView, CreateView
from django.db.models import Count, Max
from django.urls import reverse

from users.models import CustomUser
from .models import Win, Bet
from .forms import WinCreateForm

class LeagueTableView(ListView):
    model = CustomUser
    template_name = 'index.html'
    context_object_name = 'players'
    
    def get_queryset(self):
        return CustomUser.objects.annotate(num_wins=Count('wins'), last_win=Max('wins__date')).order_by('-num_wins', 'last_win').distinct()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add in custom QuerySets
        context["champions_league_players"] = CustomUser.objects.annotate(num_wins=Count('wins', distinct=True), last_win=Max('wins__date')).order_by('-num_wins', 'last_win').distinct()[:4]
        context["premier_league_players"] = CustomUser.objects.annotate(num_wins=Count('wins', distinct=True), last_win=Max('wins__date')).order_by('-num_wins', 'last_win').distinct()[4:8]
        context["championship_players"] = CustomUser.objects.annotate(num_wins=Count('wins', distinct=True), last_win=Max('wins__date')).order_by('-num_wins', 'last_win').distinct()[8:12]
        context["vanarama_players"] = CustomUser.objects.annotate(num_wins=Count('wins', distinct=True), last_win=Max('wins__date')).order_by('-num_wins', 'last_win').distinct()[12:16]

        context["monthly_leaders"] = CustomUser.objects.annotate(num_wins=Count('wins'), last_win=Max('wins__date')).filter(wins__date__contains=datetime.date.today().month).order_by('-num_wins', 'last_win').distinct()
        context["weekly_leaders"] = CustomUser.objects.annotate(num_wins=Count('wins'), last_win=Max('wins__date')).filter(wins__date__week=datetime.date.today().isocalendar()[1]).order_by('-num_wins', 'last_win').distinct()

        context["this_years_game_count"] = Win.objects.filter(date__contains=datetime.date.today().year).count()

        context["todays_result"] = Win.objects.filter(date__year=datetime.date.today().year, date__month=datetime.date.today().month, date__day=datetime.date.today().day)
        
        # Return context
        return context
    
class WinCreateView(CreateView):
    model = Win
    fields = ['winner', 'runner_up', 'participants']
    template_name = 'create_win.html'
    form = WinCreateForm
    
    def get_success_url(self):
        return reverse('home')
    
class AllGamesView(ListView):
    model = Win
    ordering = ['-date']
    template_name = 'all_games.html'
    context_object_name = 'all_games'

class AllBetsView(ListView):
    model = Bet
    template_name = 'all_bets.html'
    context_object_name = 'all_bets'