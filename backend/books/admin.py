from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(books)
admin.site.register(Users)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Ordered)