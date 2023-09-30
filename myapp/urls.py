from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('orders', views.OrderListView.as_view(), name='orders'),
    path('orders/<pk>', views.OrderDetailView.as_view(), name='order_detail'),

    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('customers/create', views.CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<pk>', views.CustomerCreateView.as_view(), name='customer_detail'),

]
