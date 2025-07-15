from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'role', 'first_name', 'last_name', 'phone_number', 'date_joined',


class UserDetailModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'role', 'phone_number', 'get_full_name'


class RegisterUserModelSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'phone_number', 'first_name', 'last_name', 'password', 'confirm_password'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password', None)
        password = attrs.get('password')

        if confirm_password != password:
            raise ValidationError("Parollar mos emas!")

        attrs['password'] = make_password(password)
        return attrs

    def create(self, validated_data):
        return super().create(validated_data)


class LoginUserModelSerializer(Serializer):
    phone_number = CharField()
    password = CharField(write_only=True)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise ValidationError("Bunday foydalanuvchi mavjud emas.")

        if not user.check_password(password):
            raise ValidationError("Parol noto‘g‘ri.")

        if not user.is_active:
            user.is_active = True
            user.save(update_fields=['is_active'])

        attrs['user'] = user
        return attrs
