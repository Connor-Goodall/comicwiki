from django import forms
from .models import superheroBiography, superheroAppearance, superheroWork, superheroConnections

class SuperheroBiographyForm(forms.ModelForm):
    class Meta:
        model = superheroBiography
        fields = ['fullName', 'alterEgos', 'aliases', 'birthPlace', 'firstAppearance', 'publisher']

class SuperheroAppearanceForm(forms.ModelForm):
    class Meta:
        model = superheroAppearance
        fields = ['gender', 'race', 'height', 'weight', 'eyeColor', 'hairColor']

class SuperheroWorkForm(forms.ModelForm):
    class Meta:
        model = superheroWork
        fields = ['occupation', 'base']

class SuperheroConnectionsForm(forms.ModelForm):
    class Meta:
        model = superheroConnections
        fields = ['groupAffiliation', 'relatives']