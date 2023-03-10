from django.contrib import admin
from .models import *
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = [
        *UserAdmin.fieldsets,
        ('Organizational info', {
            'fields': ('contactNumber', 'accountType', 'department', 'date_of_inactivity','college')
        })
    ]

admin.site.register(CustomUser, CustomUserAdmin),
admin.site.register(Student)