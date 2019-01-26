from django.urls import path
from . import views
from django.conf.urls import url

app_name="Lists"
urlpatterns = [
    path('',views.showLists,name="showLists"),
    path('createlist/',views.createList,name="createList"),
    url(r'(?P<slug>[\w-]+)/',views.displayList,name="displayList"),
]
