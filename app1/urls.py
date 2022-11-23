
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sing_up,name="sing_up"),
    path('login/', views.login_up,name="login_up"),
    path('profile/', views.user_profile,name="user_profile"),
    path('logout/', views.user_logout,name="logout"),
]