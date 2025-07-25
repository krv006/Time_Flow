from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers

from apps.models import User


class ManagerCreatesUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # oldingi ManagerUser emas
        fields = ('phone_number', 'first_name', 'password', 'process')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)


class LoginManagerUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise serializers.ValidationError("Bunday foydalanuvchi mavjud emas.")

        if not check_password(password, user.password):
            raise serializers.ValidationError("Parol noto‘g‘ri.")

        if not user.is_active:
            raise serializers.ValidationError("Foydalanuvchi faollashtirilmagan.")

        attrs["user"] = user
        return attrs
