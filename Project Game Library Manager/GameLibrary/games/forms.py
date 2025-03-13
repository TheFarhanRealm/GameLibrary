from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'release_date', 'developer', 'platform']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
        }