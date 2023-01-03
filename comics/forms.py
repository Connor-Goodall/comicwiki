from django import forms
from .models import superheroBiography, superheroAppearance

class SuperheroBiographyForm(forms.ModelForm):
    class Meta:
        model = superheroBiography
        fields = ['fullName', 'alterEgos', 'aliases', 'birthPlace', 'firstAppearance', 'publisher']

class SuperheroAppearanceForm(forms.ModelForm):
    class Meta:
        model = superheroAppearance
        fields = ['gender', 'race', 'height', 'weight', 'eyeColor', 'hairColor']