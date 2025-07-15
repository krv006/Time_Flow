from rest_framework.serializers import ModelSerializer

from apps.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'role', 'first_name', 'last_name', 'phone_number', 'date_joined',


class UserDetailModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'role', 'phone_number', 'get_full_name'

