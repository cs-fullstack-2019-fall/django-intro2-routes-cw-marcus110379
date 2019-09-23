from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gogetthegood/', views.gogettheGoods, name='go_get_the_good'),
    path('happyhappyjoyjoy/', views.happyhappyjoyJoy, name='happy_happy_joy_joy')
]

