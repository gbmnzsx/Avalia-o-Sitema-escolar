from django.urls import path

from portal import views

urlpatterns = [
    path('index/', views.index),
    path('cadastro/', views.cadastro),
]
