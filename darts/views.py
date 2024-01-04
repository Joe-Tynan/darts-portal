import datetime

from django.views.generic import ListView, CreateView
from django.db.models import Count
from django.urls import reverse

from users.models import CustomUser
from .models import Win
from .forms import WinCreateForm

class LeagueTableView(ListView):
    model = CustomUser
    template_name = 'index.html'
    context_object_name = 'players'
    
    def get_queryset(self):
        return CustomUser.objects.annotate(num_wins=Count('wins')).order_by('-num_wins')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add in custom QuerySets
        context["champions_league_players"] = CustomUser.objects.annotate(num_wins=Count('wins')).order_by('-num_wins', 'wins__date')[:4]
        context["premier_league_players"] = CustomUser.objects.annotate(num_wins=Count('wins')).order_by('-num_wins', 'wins__date')[4:8]
        context["championship_players"] = CustomUser.objects.annotate(num_wins=Count('wins')).order_by('-num_wins', 'wins__date')[8:12]
        context["vanarama_players"] = CustomUser.objects.annotate(num_wins=Count('wins')).order_by('-num_wins', 'wins__date')[12:16]

        context["monthly_leaders"] = CustomUser.objects.annotate(num_wins=Count('wins')).filter(wins__date__contains=datetime.date.today().month).order_by('-num_wins', 'wins__date')
        context["weekly_leaders"] = CustomUser.objects.annotate(num_wins=Count('wins')).filter(wins__date__week=datetime.date.today().isocalendar()[1]).order_by('-num_wins', 'wins__date')

        # Return context
        return context
    
class WinCreateView(CreateView):
    model = Win
    fields = ['winner', 'runner_up', 'participants']
    template_name = 'create_win.html'
    form = WinCreateForm
    
    def get_success_url(self):
        return reverse('home')