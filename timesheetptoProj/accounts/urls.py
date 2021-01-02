from django.urls import path
from .views import login, register, dashboard, logout
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    #need to set login redirect url in project settings: LOGIN_REDIRECT_URL = 'accounts/dashboard (need to user templates/registration/login.html)
    path('login/', LoginView.as_view(), name='login'),
    #instead of directing to django assumed-templated logout page, direct to url to 'index.html'
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    #path('login/', login, name='login'),
    path('register', register, name='register'),
    #path('logout', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]