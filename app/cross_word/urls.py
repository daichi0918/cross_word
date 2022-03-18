from django.urls import path, include
from . import views

app_name = "cross_word"

urlpatterns = [
    path('easy/', views.easy, name='easy'),
    path('easy_answer/', views.easy_answer, name='easy_answer'),
    path('easy2/', views.easy2, name='easy2'),
    path('easy_answer2/', views.easy_answer2, name='easy_answer2'),
    path('nomal/', views.nomal, name='nomal'),
    path('nomal_answer/', views.nomal_answer, name='nomal_answer'),
    path('nomal2/', views.nomal2, name='nomal2'),
    path('nomal_answer2/', views.nomal_answer2, name='nomal_answe2r'),
    path('hard/', views.hard, name='hard'),
    path('hard_answer/', views.hard_answer, name='hard_answer'),
    path('hard2/', views.hard2, name='hard2'),
    path('hard_answer2/', views.hard_answer2, name='hard_answer2'),
]