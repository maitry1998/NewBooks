from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from bookstore import views

urlpatterns = [

    path('', views.store),
    path('fiction/', views.fiction),
    url(r'^book/(\d+)', views.book_detail, name='book_details'),
]
