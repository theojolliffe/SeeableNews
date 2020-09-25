from django.urls import path

from . import views

urlpatterns = [
    path('liverpool', views.liverpool, name='liverpool'),
    path('SpursVShkendija', views.spursVShkendija, name='SpursVShkendija'),
    path('SpursVSoton', views.spursVSoton, name='SpursVSoton'),
    path('LiverpoolVChelsea', views.liverpoolVChelsea, name='LiverpoolVChelsea'),
    path('spurs', views.spurs, name='spurs'),
    path('teams', views.teams, name='teams'),
    path('players', views.players, name='players'),
    path('SpursCB', views.skriniar, name='SpursCB'),
    path('', views.home, name='home'),
]