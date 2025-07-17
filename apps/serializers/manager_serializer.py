from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.models import ManagerUser


class RegisterManagerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerUser
        fields = ('name', 'phone_number', 'password', 'process', 'created_at')
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        return ManagerUser.objects.create_user(**validated_data)


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
