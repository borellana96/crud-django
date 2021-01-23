from django.urls import path
from .views import signup, signin, logoutUser#, default

urlpatterns = [
    #path('', default, name="default"),
    path('register/<int:tipo_id>', signup, name="signup"),
    path('login/<int:tipo_id>', signin, name="signin"),
    path('logout', logoutUser, name="logout")
]
