from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import JokeText
from uuid import uuid4


class SignUpForm(forms.ModelForm):

    class Meta:
        model = JokeText
        fields = ('joke_text', 'joke_id')
