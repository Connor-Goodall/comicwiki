from django.urls import path
from . import views
app_name = 'comics'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<name>/', views.characterInfo, name = 'characterInfo'),
]