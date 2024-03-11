from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product_materials.models import ProductMaterials
from warehouses.api.v1.serializer import ProductMaterialSerializer, ProductSerializer
from warehouses.models import Warehouses


class ProductMaterialAPIView(APIView):

    def get(self, request):
        serializer_data = []

        for product, qty in request.GET.items():
            # filter from db Product
            product_obj = Product.objects.filter(name__iexact=product).first()

            serializer = ProductSerializer(product_obj, context={'product_name': product, 'product_qty': qty})

            if serializer:
                serializer_data.append(serializer.data)
            else:
                # Handle invalid data, maybe return error response
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'result': serializer_data}, status=status.HTTP_200_OK)
