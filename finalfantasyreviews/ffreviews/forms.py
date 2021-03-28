from django import forms
from .models import ffGame, ffReview

class GameForm(forms.ModelForm):
    class Meta:
        model=ffGame
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=ffReview
        fields='__all__'

