from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logut', views.logout_user, name="logout_user"),
    path('dashboard', views.dashboard, name="dashboard"),

]
