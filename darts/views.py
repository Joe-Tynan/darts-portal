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
        #return CustomUser.objects.exclude(plays_darts=False).annotate(num_wins=Count('wins', distinct=True), last_win=Max('wins__date')).order_by('-num_wins', 'last_win').distinct()
    
        return CustomUser.objects.exclude(plays_darts=False).annotate(num_wins=Count('wins', distinct=True), num_runner_ups=Count('runner_ups', distinct=True), last_win=Max('wins__date'), last_runner_up=Max('runner_ups__date'), num_games_played=Count('games_played', distinct=True)).order_by('-num_wins', 'last_win', '-num_runner_ups', 'last_runner_up', '-num_games_played', 'first_name', 'last_name').distinct()
    
    def get(self, request, *args, **kwargs):
        # Call the base implementation
        get = super().get(request, *args, **kwargs)

        # Set Up Sessions Framework
        visit_count = request.session.get('visit_count', 0)
        request.session['visit_count'] = visit_count + 1

        # Return Get
        return get

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add in custom QuerySets
        context["monthly_leaders"] = CustomUser.objects.exclude(plays_darts=False).annotate(num_wins=Count('wins'), last_win=Max('wins__date')).filter(wins__date__month=datetime.date.today().month).order_by('-num_wins', 'last_win').distinct()[:3]

        context["weekly_leaders"] = CustomUser.objects.exclude(plays_darts=False).annotate(num_wins=Count('wins'), last_win=Max('wins__date')).filter(wins__date__week=datetime.date.today().isocalendar()[1]).order_by('-num_wins', 'last_win').distinct()[:3]

        context["this_years_game_count"] = Win.objects.filter(date__contains=datetime.date.today().year).count()

        context["last_result"] = Win.objects.order_by('-date')[:1]

        context["top_5_form"] = sorted( CustomUser.objects.exclude(plays_darts=False), key=lambda u: u.get_form_score(), reverse=True )[:5]
        context["top_5_win_ratio"] = sorted( CustomUser.objects.exclude(plays_darts=False), key=lambda u: u.get_win_ratio(), reverse=True )[:5]
        
        # Return context
        return context
    
class WinCreateView(CreateView):
    model = Win
    fields = ['winner', 'runner_up', 'participants']
    template_name = 'create_win.html'
    form = WinCreateForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add in custom QuerySets
        context["last_result"] = Win.objects.order_by('-date')[:1]
        
        # Return context
        return context
    
    def get_success_url(self):
        return reverse('darts:home')
    
class AllGamesView(ListView):
    model = Win
    ordering = ['-date']
    template_name = 'all_games.html'
    context_object_name = 'all_games'

class AllBetsView(ListView):
    model = Bet
    template_name = 'all_bets.html'
    context_object_name = 'all_bets'