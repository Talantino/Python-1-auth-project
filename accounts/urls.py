from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name=""),
    path('register/', views.register, name="register"),
    path('login/', views.my_login, name="login"),
    path('user-logout/', views.user_logout, name="user-logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
