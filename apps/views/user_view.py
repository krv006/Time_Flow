from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework_simplejwt.tokens import RefreshToken

from apps.models import User
from apps.serializers import UserModelSerializer, RegisterUserModelSerializer, LoginUserModelSerializer


@extend_schema(tags=["User"], description="User lardi olish")
class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(
    tags=["Auth"],
    description="Foydalanuvchini telefon raqam orqali ro‘yxatdan o‘tkazish.",
    request=RegisterUserModelSerializer
)
class RegisterAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserModelSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "message": "Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi.",
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
    tags=["Auth"],
    description="Foydalanuvchini telefon raqami orqali tizimga kiritish.",
    request=LoginUserModelSerializer
)
class LoginAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginUserModelSerializer
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
