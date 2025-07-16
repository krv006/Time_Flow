from rest_framework.serializers import ModelSerializer

from apps.models import Product, Process


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'process')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['process'] = ProcessModelSerializer(instance.process).data
        return repr


class ProcessModelSerializer(ModelSerializer):
    class Meta:
        model = Process
        fields = ('id', 'name', 'manager')

    def to_representation(self, instance):
        from apps.serializers import UserDetailModelSerializer
        repr = super().to_representation(instance)
        repr['manager'] = UserDetailModelSerializer(instance.manager).data
        return repr
