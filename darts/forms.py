from django import forms

from users.models import CustomUser
from .models import Win

class WinCreateForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.exclude(plays_darts=False),
        widget=forms.CheckboxSelectMultiple(),
        label="All Participants",
    )

    class Meta:
        model = Win
        fields = ['winner', 'runner_up', 'participants']