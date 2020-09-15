from django.forms import ModelForm
from .models import Trivia
from django import forms
from . import models

class TriviaForm(forms.ModelForm):
    class Meta:
        model=models.Trivia
        fields='__all__'


class OptionForm(forms.ModelForm):
    class Meta:
        model=models.Option
        fields='__all__'


class PlayerForm(forms.ModelForm):
    name = forms.CharField(required = True)
    class Meta:
        model=models.Player
        fields='__all__'
