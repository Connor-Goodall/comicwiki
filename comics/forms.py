from django import forms
from .models import superheroBiography, superheroAppearance, superheroWork, superheroConnections, superheroPowerstats, superheroImages

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

class SuperheroPowerstatsForm(forms.ModelForm):
    class Meta:
        model = superheroPowerstats
        fields = ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']

class SuperheroImagesForm(forms.ModelForm):
    class Meta:
        model = superheroImages
        fields = ['medium']

class SuperheroNameForm(forms.ModelForm):
    class Meta:
        model = superheroBiography
        fields = ['name']

class SuperheroCreationForm(forms.ModelForm):
    alignment_choices = [('good', 'Hero'), ('bad', 'Villian'), ('neutral', 'Anti-hero')]
    alignment = forms.CharField(label = "What is the character's alignment?", widget = forms.Select(
        choices = alignment_choices))
    class Meta:
        model = superheroBiography
        fields = ['name', 'alignment']