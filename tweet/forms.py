from django import forms
from .models import Tweet , Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Tweetform(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class Profileform(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("profile_photo","bio")
