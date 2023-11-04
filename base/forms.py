from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'username'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'id': 'email'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'id': 'password1'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'id': 'password2'})
    )

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']  # Include only the required fields
        exclude = ['first_name', 'last_name', 'bio']  # Exclude non-required fields


class RoomForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'name'})
    )
    room_type = forms.ModelChoiceField(
        label="Type",
        queryset=Type.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control form-control-lg',
                                   'id': 'room_type',
                                   'title': 'Press to choose MOVIE or SERIES'
                                   })
    )
    description = forms.CharField(
        label="Topic",
        widget=forms.Textarea(attrs={'class': 'form-control form-control-lg', 'id': 'description', 'rows': 2})
    )
    category = forms.ModelMultipleChoiceField(
        label="Categories",
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-lg select',
                                           'id': 'category',
                                           'title': 'Press Ctrl to select multiple categories'
                                           })
    )

    class Meta:
        model = Room
        fields = ['name', 'room_type', 'description', 'category']

