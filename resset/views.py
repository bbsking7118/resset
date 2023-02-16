from django.shortcuts import render, get_object_or_404

from .models import *
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOnly, IsOwnerOrReadOnly

def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'resset/list.html',
                  {'current_category': current_category, 'categories': categories, 'products': products})

# from cart.forms import AddProductForm
def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    return render(request, 'resset/detail.html', {'product': product})
    # add_to_cart = AddProductForm(initial={'quantity':1})
    # return render(request, 'shop/detail.html', {'product': product, 'add_to_cart':add_to_cart})

class ProductList(generics.ListCreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer