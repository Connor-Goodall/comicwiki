from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'comics'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('allcharacters/', views.allCharacters, name='allCharacters'),
    path('marvelcharacters/', views.marvelCharacters, name = 'marvelCharacters'),
    path('dccharacters/', views.dcCharacters, name = 'dcCharacters'),
    path('othercharacters/', views.otherCharacters, name = 'otherCharacters'),
    path('results/', views.SearchResultsView.as_view(), name = "searchResults"),
    path('add/', views.addCharacter, name = 'addCharacter'),
    path('<name>/edit/', views.edit, name = 'edit'),
    path('<name>/', views.characterInfo, name='characterInfo'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)