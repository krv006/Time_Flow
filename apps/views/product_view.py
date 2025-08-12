from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models import Process, Product
from apps.permission import IsManager
from apps.serializers import ProcessModelSerializer
from apps.serializers.product_serializer import ProductModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (IsAuthenticated, IsManager)
    search_fields = ('name', 'process__name')
    filterset_fields = ('name', 'process')


class ProcessListCreateAPIView(ListCreateAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessModelSerializer
    permission_classes = (IsAuthenticated, IsManager)
    search_fields = ('name', 'manager__phone_number')
    filterset_fields = ('name', 'manager')
