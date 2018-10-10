from django.urls import path

from . import views

app_name = 'youtubeplayer'
urlpatterns = [
    path('new', views.new_list, name='new_list'),
    path('<int:list_id>/', views.view_list, name='view_list'),
    path('<int:list_id>/add_item', views.add_item, name='add_item'),
    path('add', views.add, name='add'),
    path('queue', views.queue, name='queue'),
]
