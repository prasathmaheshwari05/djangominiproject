from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('image/<int:pk>/', views.detail, name='detail'),
    path('add/', views.add_image, name='add_image'),
]
