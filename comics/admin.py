from django.contrib import admin
from .models import superheroBiography, superheroAppearance, superheroWork, superheroConnections, superheroPowerstats
from .models import superheroImages

# Register your models here.
admin.site.register(superheroBiography)
admin.site.register(superheroAppearance)
admin.site.register(superheroWork)
admin.site.register(superheroConnections)
admin.site.register(superheroPowerstats)
admin.site.register(superheroImages)