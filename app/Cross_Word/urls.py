from django.urls import path, include
from . import views

app_name = "cross_word"

urlpatterns = [
    path('', views.index, name='index'),
    path('answer1/', views.answer1, name='answer1')
]