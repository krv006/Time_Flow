from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.models import Process, Product
from apps.serializers import ProcessModelSerializer
from apps.serializers.product_serializer import ProductModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (AllowAny,)


class ProcessListCreateAPIView(ListCreateAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessModelSerializer
    permission_classes = (AllowAny,)
