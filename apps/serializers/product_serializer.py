from rest_framework.serializers import ModelSerializer

from apps.models.product_model import Process
from apps.serializers import UserDetailModelSerializer


class ProcessModelSerializer(ModelSerializer):
    class Meta:
        model = Process
        fields = ('id', 'name', 'user')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['user'] = UserDetailModelSerializer(instance.user).data
        return repr
