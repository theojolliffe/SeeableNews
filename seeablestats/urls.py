from django.urls import path

from . import views

urlpatterns = [
    path('ndombele', views.ndombele, name='ndombele'),
    path('soton', views.soton, name='soton'),
    path('spurs', views.spurs, name='spurs'),
    path('', views.home, name='home'),
]