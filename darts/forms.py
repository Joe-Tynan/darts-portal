from django import forms

from users.models import CustomUser


class WinCreateForm(forms.Form):
    participants = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.exclude(plays_darts=False),
        widget=forms.CheckboxSelectMultiple(),
    )
