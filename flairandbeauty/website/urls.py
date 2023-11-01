from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('jobs', views.jobs, name='jobs'),
    path('team', views.team, name='team'),
    path('booking', views.booking, name= 'booking'),
]