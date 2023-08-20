from django.urls import path 
from . import views


urlpatterns = [
    path('',view=views.index,name="index"),
    path('user_info.html',view=views.user_info,name="user_info"),
    path('boking.html',view=views.boking,name="boking"),
    path('bill.html',view=views.bill,name="pyment"),
]