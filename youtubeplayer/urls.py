from django.urls import path

from . import views

app_name = 'youtubeplayer'
urlpatterns = [
    path('', views.index, name='index'),
]
