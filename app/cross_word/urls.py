from django.urls import path, include
from . import views

app_name = "cross_word"

urlpatterns = [
    path('easy/', views.easy, name='easy'),
    path('easy_answer/', views.easy_answer, name='easy_answer'),
    path('nomal/', views.nomal, name='nomal'),
    path('nomal_answer/', views.nomal_answer, name='nomal_answer'),
    path('hard/', views.hard, name='hard'),
    path('hard_answer/', views.hard_answer, name='hard_answer'),
]