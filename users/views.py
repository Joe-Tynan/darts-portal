from django.views.generic import DetailView

from .models import CustomUser

# Create your views here.
class PlayerDetailView(DetailView):
    model = CustomUser
    template_name = 'players/detail.html'
    context_object_name = 'player'