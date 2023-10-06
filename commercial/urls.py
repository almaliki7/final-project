from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('specialoffer/', views.specialoffer, name='specialoffer'),
    path('room/', views.room, name='room'),
    path('style/', views.style, name='style'),
    path('coffeebreak/', views.coffeebreak, name='coffeebreak'),
    path('reservation/', views.reservation, name='reservation'),
    path('contactUs/', views.contactUs, name='contactUs')
]

