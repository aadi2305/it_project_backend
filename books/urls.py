from django.urls import path
from .views import yo,CreateUser,SendToOrderedList,removeFromCart, CreateAddress, searchByName, searchByGenre, sendCartInfo, addToCartInfo, addToWishlist, sendWishlistInfo, addToOrderedList, SendAllBooks 
urlpatterns = [
    path("",yo),
    path('AllBooks', SendAllBooks),
    path('CreateUser', CreateUser.as_view()),
    path('CreateAddress', CreateAddress.as_view()),
    path('Search', searchByName.as_view()),
    path('SearchByGenre', searchByGenre.as_view()),
    path('SendCartInfo', sendCartInfo.as_view()),
    path('AddToCart', addToCartInfo.as_view()),
    path('AddtoWishlist',addToWishlist.as_view()),
    path('SendWishlistInfo',sendWishlistInfo.as_view()),
    path('AddToOrderedList',addToOrderedList.as_view()),
    path('SendToOrderedList',SendToOrderedList.as_view()),
    path("RemoveFromCart",addToOrderedList.as_view()),
]
