from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.models import ManagerUser


class ManagerCreatesUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerUser
        fields = ('phone_number', 'name', 'password', 'process')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return ManagerUser.objects.create(**validated_data)


class LoginManagerUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        user = authenticate(username=phone_number, password=password)

        if not user:
            raise serializers.ValidationError("Telefon raqam yoki parol noto‘g‘ri.")
        if not isinstance(user, ManagerUser):
            raise serializers.ValidationError("Siz manager emassiz.")
        if not user.is_active:
            raise serializers.ValidationError("Foydalanuvchi aktiv emas.")

        attrs["user"] = user
        return attrs
