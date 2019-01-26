from django.urls import path
from . import views

app_name="Lists"
urlpatterns = [
    path('',views.showLists,name="showLists"),
    path('createlist/',views.createList,name="createList"),
]
