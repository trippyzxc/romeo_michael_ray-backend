from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductsSerializer
from .models import Products

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class ProductUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer