from django.urls import path
from . import views

app_name = "level"

urlpatterns = [
    path('', views.index, name='index'),
    # path('base/', views.base, name='base'),
    path('select/', views.select, name='select'),
    path('easy/', views.easy, name='easy'),
    path('nomal/', views.nomal, name='nomal'),
    path('hard/', views.hard, name='hard'),
    # path('cross_word', views.cross_word, name='cross_word'),
]