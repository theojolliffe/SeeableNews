from django.urls import path

from . import views

urlpatterns = [
    path('ndombele', views.ndombele, name='ndombele'),
    path('soton', views.soton, name='soton'),
    path('SpursVSoton', views.spursVSoton, name='spursvsoton'),
    path('spurs', views.spurs, name='spurs'),
    path('teams', views.teams, name='teams'),
    path('', views.home, name='home'),
]