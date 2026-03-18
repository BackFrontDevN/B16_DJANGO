from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Category,Movie,Genre

class MovieForm(forms.ModelForm):
    name = forms.CharField(
        label="Movie Name",
        widget=forms.TextInput(attrs={"class": "movie-input"})
    )
    description = forms.CharField(
        label="Описание",
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    class Meta:
        model = Movie
        fields = "__all__"

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password"
    }))

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"