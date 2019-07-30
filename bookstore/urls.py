from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from bookstore import views

urlpatterns = [

    path('', views.store),
    path('fiction/', views.fiction),
    url(r'^book/(\d+)', views.book_detail, name='book_details'),
    url(r'^add/(\d+)', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/', views.cart, name='cart'),
]
