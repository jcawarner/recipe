from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('random/', views.random, name="random"),
    path('search/', views.search, name="search"),
    path('get_recipe/', views.get_recipe, name='get_recipe'),
    ]
