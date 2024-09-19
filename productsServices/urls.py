from django.urls import path
from .api.viewset import product_list, product_detail

app_name = 'productsServices'
urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
]
