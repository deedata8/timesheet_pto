from django.urls import path
from .views import register, dashboard, index
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    #need to set login & logout redirect url in project settings: LOGIN_REDIRECT_URL = 'accounts/dashboard (need to user templates/registration/login.html)
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('index', index, name='home'),
]