from django.conf.urls import url
from django.urls import path

from . import consumers

# websocket_urlpatterns = [
#     url(r'^ws/playlist/(?P<room_name>[^/]+)/$', consumers.PlaylistConsumer)
# ]

websocket_urlpatterns = [
    path('ws/playlist/<str:room_name>/', consumers.PlaylistConsumer)
]