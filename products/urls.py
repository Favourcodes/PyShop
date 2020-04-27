from django.urls import path
from . import views  # the period (.) means 'the current folder'


urlpatterns = [
    path('', views.index),
    path('new', views.new)
]



