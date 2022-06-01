from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile, Role
User = get_user_model()


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Username"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "email",
        "placeholder": "Email"
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Password"
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Confirm Password"
    }))

    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "email",
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',  'email']


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "type": "text",
    }))

    class Meta:
        model = Profile
        abstract = False
        fields = ['bio', 'image', 'active']


class RoleForm(forms.ModelForm):
    role = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text"
    }))

    class Meta:
        model = Role
        fields = ['role', 'creator', 'createDate']


class AllUsersForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['is_admin', 'is_superadmin', 'roles']