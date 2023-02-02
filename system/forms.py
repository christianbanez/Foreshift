from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.forms import SetPasswordForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

class CreateUser(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ['first_name', 'last_name', 'email', 'username']

		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Juan'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Dela Cruz'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g., juandelacruz@email.com'}),
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., juanDC'})
		}
	
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SetPassword(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))