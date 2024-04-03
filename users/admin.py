from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = ['username', 'first_name', 'last_name', 'nickname']

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ["nickname", "plays_darts", "does_karting"]}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ["nickname", "plays_darts", "does_karting"]}),)

admin.site.register(get_user_model(), CustomUserAdmin)