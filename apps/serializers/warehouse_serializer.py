from rest_framework.serializers import ModelSerializer

from apps.models import Material
from apps.models.warehouse_model import Processing


class MaterialModelSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = 'id', 'name'


class ProcessingModelSerializer(ModelSerializer):
    class Meta:
        model = Processing
        fields = ('id', 'processing', 'data', 'created_at', 'material', 'user')
