from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
]