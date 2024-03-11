from django.urls import path

from .views import *

urlpatterns = [
    path('product-material/', ProductMaterialAPIView.as_view(), name='product_material'),
]
