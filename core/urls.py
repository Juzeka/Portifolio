from django.urls import path

from core import views

urlpatterns = [
    path('', views.home, name='index'),
    path('contato', views.contato, name='contato'),
    
]