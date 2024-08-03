from django.views.generic import DetailView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CustomUser

# Create your views here.
@api_view()
def all_players_api_view(request):
    return Response({'message': 'Test!'})

class PlayerDetailView(DetailView):
    model = CustomUser
    template_name = 'players/detail.html'
    context_object_name = 'player'