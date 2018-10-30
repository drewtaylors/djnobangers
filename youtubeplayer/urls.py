from django.urls import path

from . import views

app_name = 'youtubeplayer'
urlpatterns = [
    path('new', views.new_list, name='new_list'),
    path('<int:list_id>/', views.view_list, name='view_list'),
    path('<int:list_id>/add_url', views.add_url, name='add_url'),
]
