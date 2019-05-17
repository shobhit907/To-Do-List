from django.conf.urls import url
from django.urls import path,include
from . import views

app_name='accounts'

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    url('auth/',include('social_django.urls',namespace='accounts:social')),
]
