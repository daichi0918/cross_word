from django.urls import path
from .views import (
    RegistUserView, HomeView, UserLoginView,
    UserLogoutView, UserView
)

app_name = 'user'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('regist/', RegistUserView.as_view(), name='regist'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('users/', UserView.as_view(), name='users'),
]
