from django import forms

from users.models import CustomUser

class WinCreateForm(forms.Form):
    participants = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(), widget=forms.CheckboxSelectMultiple)