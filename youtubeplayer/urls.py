from django.urls import path

from . import views

app_name = 'youtubeplayer'
urlpatterns = [
    path('', views.index, name='index'),
    path('youtubeplayer/the-only-list-in-the-world/', views.view_list, name='view_list'),
    path('add', views.add, name='add'),
    path('queue', views.queue, name='queue'),
]
