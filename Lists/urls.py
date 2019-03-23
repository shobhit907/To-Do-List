from django.urls import path,include
from . import views
from django.conf.urls import url

app_name="Lists"
urlpatterns = [
    path('',views.showLists,name="showLists"),
    path('createlist/',views.createList,name="createList"),
    url(r'^(?P<slug>[\w-]+)/$',views.displayList,name="displayList"),
    url(r'^(?P<slug>[\w-]+)/additem/',views.addItem,name="addItem"),
    url(r'^(?P<slug>[\w-]+)/(?P<slug1>[\w-]+)/$',views.showItem,name="showItem"),
    url(r'^(?P<slug>[\w-]+)/(?P<slug1>[\w-]+)/deleteitem/$',views.deleteItem,name="deleteItem"),
]
