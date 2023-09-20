from django.urls import path
from .views import ProductListCreateView, ProductUpdateDeleteView

urlpatterns = [
    path('fetch-create/', ProductListCreateView.as_view(), name= 'product-list-create'),
    path('update-delete/<int:pk>/', ProductUpdateDeleteView.as_view(), name='product-update-delete')
]