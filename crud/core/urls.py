from django.urls import path
from .views import default,home, manage, create, read, update, delete, vender, contact

urlpatterns = [ #   URL Name, Associated View, 
    path('', default, name ="default"),
    path('home', home, name ="home"),  #debe ir el / porque sino lo concatena
    path('manageProduct', manage, name="manage"),
    path('createProduct', create, name="create"),
    path('readProduct', read, name="read"),
    path('updateProduct/<id>', update, name="update"),
    path('deleteProduct/<id>', delete, name="delete"),
    path('venderProduct', vender, name="vender"),
    path('contact', contact, name="contact"),
]
