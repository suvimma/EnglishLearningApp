# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Flashcard, Word
from captcha.fields import CaptchaField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'captcha']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['english_word', 'polish_word']

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['english_word', 'polish_word', 'level', 'category']
