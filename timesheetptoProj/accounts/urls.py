from django.urls import path
from .views import login, register, dashboard, logout

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
]