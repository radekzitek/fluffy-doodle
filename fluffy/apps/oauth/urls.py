from django.urls import path
from . import views

urlpatterns = [
    path('token/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('jwt/refresh/', views.refresh_token, name='refresh_token'),
    path('password/reset/', views.password_reset_request, name='password_reset_request'),
    path('password/reset/confirm/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password/change/', views.password_change, name='password_change'),
]
