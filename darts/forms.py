from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from users.models import CustomUser
from .models import Win

class WinCreateForm(forms.ModelForm):
    winner = forms.ModelChoiceField(
        queryset=CustomUser.objects.exclude(plays_darts=False),
        required=True
    )
    runner_up = forms.ModelChoiceField(
        queryset=CustomUser.objects.exclude(plays_darts=False),
        required=True
    )
    participants = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.exclude(plays_darts=False),
        widget=forms.CheckboxSelectMultiple(),
        label="All Participants",
        required=True
    )

    class Meta:
        model = Win
        fields = ['winner', 'runner_up', 'participants']

    def clean(self):
        # Overall Form Validation
        cleaned_data = super().clean()
        winner = cleaned_data.get('winner')
        runner_up = cleaned_data.get('runner_up')
        participants = cleaned_data.get('participants')

        if not participants:
            raise ValidationError('You obviously need to add participants you weapon!')

        # 1. The winner and runner up can't be the same
        if winner and runner_up and winner == runner_up:
            raise ValidationError('The winner and runner up have to be different people you donut!')

        # 2. Winner and runner up must be selected as participants
        if winner and winner not in participants:
            raise ValidationError('What are you doing? Include the winner in the participants!')

        if runner_up and runner_up not in participants:
            raise ValidationError('What are you doing? Include the runner up in the participants!')

        # 3. At least 3 participants must be selected
        if participants and len(participants) < 3:
            raise ValidationError('Stop trying to get an easy point Bray. There has to be at least 3 people in a game!')

        #4 Only one submission can be done per day
        if Win.objects.filter(date=now().date()).exists():
            raise ValidationError('A game has already been submitted today. Pay attention you wet wipe!')

        return cleaned_data