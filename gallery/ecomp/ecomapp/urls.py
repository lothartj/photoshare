from . import views
from django.urls import path

urlpatterns = [
    path('', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.user_home, name='home')
    

]
