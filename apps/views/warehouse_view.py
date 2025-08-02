from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models import Material
from apps.models.warehouse_model import Processing
from apps.permission import IsWarehouseman
from apps.serializers import MaterialModelSerializer, ProcessingModelSerializer


class MaterialListCreateAPIView(ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialModelSerializer
    permission_classes = (IsAuthenticated, IsWarehouseman)


class ProcessingListCreateAPIView(ListCreateAPIView):
    queryset = Processing.objects.all()
    serializer_class = ProcessingModelSerializer
    permission_classes = (IsAuthenticated, IsWarehouseman)

    def get_queryset(self):
        return Processing.objects.exclude(user__role='warehouseman')
