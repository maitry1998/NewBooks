from django.contrib import admin
from django.urls import path
from bookstore import views

urlpatterns = [

    path('', views.store),
    path('fiction/', views.fiction)
]
