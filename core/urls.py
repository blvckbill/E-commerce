from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='homepage'),
    path('products/', views.product_page,name='products'),
    path('checkout/', views.checkout, name='checkout'),
]