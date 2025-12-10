from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   # ROTA DA PÁGINA INICIAL
    path('login/', views.login, name='login'),
]
