from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework_simplejwt.tokens import RefreshToken

from apps.models import ManagerUser
from apps.serializers import RegisterManagerUserSerializer, LoginManagerUserSerializer


@extend_schema(
    tags=["Manager Auth"],
    description="Manager foydalanuvchini ro‘yxatdan o‘tkazish.",
    request=RegisterManagerUserSerializer,
)
class ManagerRegisterAPIView(GenericAPIView):
    queryset = ManagerUser.objects.all()
    serializer_class = RegisterManagerUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "message": "Manager foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi.",
                "user": {
                    "id": user.id,
                    "phone_number": user.phone_number,
                    "full_name": f"{user.first_name} {user.last_name}",
                    "is_active": user.is_active,
                }
            },
            status=HTTP_201_CREATED
        )


@extend_schema(
    tags=["Manager Auth"],
    description="Manager foydalanuvchini tizimga kiritish (login).",
    request=LoginManagerUserSerializer,
)
class ManagerLoginAPIView(GenericAPIView):
    queryset = ManagerUser.objects.all()
    serializer_class = LoginManagerUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                "access": str(tokens.access_token),
                "refresh": str(tokens),
            },
            status=HTTP_200_OK
        )
