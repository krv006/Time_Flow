from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models import Material
from apps.models.warehouse_model import Processing
from apps.permission import IsWarehouseman
from apps.serializers import MaterialModelSerializer, ProcessingModelSerializer


@extend_schema(
    tags=["Warehouse"],
    description="Warehouse qismi.",
    request=MaterialModelSerializer
)
class MaterialListCreateAPIView(ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialModelSerializer
    permission_classes = (IsAuthenticated, IsWarehouseman)
    search_fields = ('name',)
    filterset_fields = ('name',)


@extend_schema(
    tags=["Warehouse"],
    description="Warehouse qismi.",
    request=ProcessingModelSerializer
)
class ProcessingListCreateAPIView(ListCreateAPIView):
    queryset = Processing.objects.all()
    serializer_class = ProcessingModelSerializer
    permission_classes = (IsAuthenticated, IsWarehouseman)
    search_fields = (
        'processing',
        'material__name',
        'data',
    )
    filterset_fields = ['processing', 'data', 'material']

    def get_queryset(self):
        return Processing.objects.exclude(user__role='warehouseman')


@extend_schema(
    tags=["Warehouse"],
    description="Warehouse qismi.",
    request=ProcessingModelSerializer
)
class ProcessingDestroyAPIView(DestroyAPIView):
    serializer_class = ProcessingModelSerializer
    lookup_field = 'id'


@extend_schema(
    tags=["Warehouse"],
    description="Warehouse qismi.",
    request=ProcessingModelSerializer
)
class ProcessingUpdateAPIView(UpdateAPIView):
    serializer_class = ProcessingModelSerializer
    lookup_field = 'id'
