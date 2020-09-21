from django.urls import path

from . import views

urlpatterns = [
    path('ndombele', views.ndombele, name='ndombele'),
    path('soton', views.soton, name='soton'),
    path('SpursVsSoton2', views.spursVSoton, name='spursvssoton2'),
    path('spurs', views.spurs, name='spurs'),
    path('teams', views.teams, name='teams'),
    path('', views.home, name='home'),
]