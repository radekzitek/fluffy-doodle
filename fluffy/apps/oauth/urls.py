from django.urls import path
from . import views

urlpatterns = [
    path('token/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('jwt/refresh/', views.refresh_token, name='refresh_token'),
]
