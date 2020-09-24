from django.urls import path

from . import views

urlpatterns = [
    path('ndombele', views.ndombele, name='ndombele'),
    path('liverpool', views.liverpool, name='liverpool'),
    path('SpursVSoton', views.spursVSoton, name='SpursVSoton'),
    path('LiverpoolVChelsea', views.liverpoolVChelsea, name='LiverpoolVChelsea'),
    path('spurs', views.spurs, name='spurs'),
    path('teams', views.teams, name='teams'),
    path('players', views.players, name='players'),
    path('Skriniar', views.skriniar, name='Skriniar'),
    path('', views.home, name='home'),
]