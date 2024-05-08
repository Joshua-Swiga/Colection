from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateRoom, name='create-room'), # The route responsible for creating rooms
    path('<int:room_name>/<int:username>', views.MessageView, name='room')
]