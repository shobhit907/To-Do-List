from django.conf.urls import url
from django.urls import path
from . import views

app_name="list"

urlpatterns = [
    path('',views.showlist,name="showlist"),
    path('additem/',views.additem,name="additem"),
]
