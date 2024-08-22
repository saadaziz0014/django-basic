from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('shirts/', views.Shirts, name='shirts'),
    path('shirt/<int:shirt_id>/', views.Shirt, name='shirt'),
]
