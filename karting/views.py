from django.views.generic import ListView

from users.models import CustomUser

class LapTimeTableView(ListView):
    model = CustomUser
    template_name = 'karting/index.html'
    context_object_name = 'drivers'
    
    def get_queryset(self):
        return CustomUser.objects.exclude(does_karting=False)