from django.urls import path
from .views import yo,CreateRoomView
urlpatterns = [
    path("",yo),
    path('sad', CreateRoomView.as_view())
]
