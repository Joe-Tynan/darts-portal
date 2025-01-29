from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = ['username', 'first_name', 'last_name', 'nickname', 'display_user_wins']
    list_filter = ('plays_darts',)

    fieldsets = UserAdmin.fieldsets + (('Darts Information', {"fields": ["nickname", "plays_darts"]}),)
    add_fieldsets = UserAdmin.add_fieldsets + (('Darts Information', {"fields": ["nickname", "plays_darts"]}),)

    # Doesn't Work on Custom User for Some Reason?
    # fields = [('first_name', 'nickname', 'last_name')]

admin.site.register(get_user_model(), CustomUserAdmin)