# soundboard/urls.py
# URL configuration for soundboard program
# Last modified: 12/28/2021

from django.urls import path
from . import views

app_name = 'soundboard'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:soundboard_id>/', views.view_soundboard, name='soundboard-view')
]