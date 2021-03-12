from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='board-home'),
    path('about/', views.about, name='board-about'),
    path('contact/', views.contact, name='board-contact'),
    path('shop/', views.shop, name='board-shop'),
]
