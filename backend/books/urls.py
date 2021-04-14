from django.urls import path
from .views import yo,CreateUser, CreateAddress, searchByName, searchByGenre
urlpatterns = [
    path("",yo),
    path('CreateUser', CreateUser.as_view()),
    path('CreateAddress', CreateAddress.as_view()),
    path('Search', searchByName.as_view()),
    path('SearchByGenre', searchByGenre.as_view())
]
