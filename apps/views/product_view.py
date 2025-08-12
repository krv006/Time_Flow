from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models import Process, Product
from apps.permission import IsManager
from apps.serializers import ProcessModelSerializer
from apps.serializers.product_serializer import ProductModelSerializer


@extend_schema(
    tags=["Product"],
    description="Manager tomonidan yangi foydalanuvchi yaratish.",
    request=ProductModelSerializer,
)
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (IsAuthenticated, IsManager)
    search_fields = ('name', 'process__name')
    filterset_fields = ('name', 'process')


@extend_schema(
    tags=["Product"],
    description="Manager tomonidan yangi foydalanuvchi yaratish.",
    request=ProcessModelSerializer,
)
class ProcessListCreateAPIView(ListCreateAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessModelSerializer
    permission_classes = (IsAuthenticated, IsManager)
    search_fields = ('name', 'manager__phone_number')
    filterset_fields = ('name', 'manager')


@extend_schema(
    tags=["Product"],
    description="Manager tomonidan yangi foydalanuvchi yaratish.",
    request=ProductModelSerializer,
)
class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductModelSerializer
    permission_classes = (IsAuthenticated, IsManager)
    lookup_field = 'id'


@extend_schema(
    tags=["Product"],
    description="Manager tomonidan yangi foydalanuvchi yaratish.",
    request=ProcessModelSerializer,
)
class ProcessDestroyAPIView(DestroyAPIView):
    serializer_class = ProcessModelSerializer
    permission_classes = (IsAuthenticated, IsManager)
    lookup_field = 'id'
