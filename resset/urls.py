from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

app_name = 'shop'

urlpatterns = [
    path('product/', ProductList.as_view()),
    path('procuct/<int:pk>/', ProductDetail.as_view()),

    path('<slug:category_slug>/', product_in_category, name='product_in_category'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),

    path('', product_in_category, name='product_all'),
]