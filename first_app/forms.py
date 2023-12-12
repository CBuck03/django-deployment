from django import forms
from django.core import validators
from . import models
from django.contrib.auth.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = models.Users
        fields = '__all__'


class NewUserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = models.UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
