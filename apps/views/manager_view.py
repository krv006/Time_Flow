from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework_simplejwt.tokens import RefreshToken

from apps.models import User  # ManagerUser emas
from apps.permission import IsManager
from apps.serializers import ManagerCreatesUserSerializer, LoginManagerUserSerializer


@extend_schema(
    tags=["Manager Auth"],
    description="Manager tomonidan yangi foydalanuvchi yaratish.",
    request=ManagerCreatesUserSerializer,
    responses={201: ManagerCreatesUserSerializer}
)
class ManagerCreatesUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ManagerCreatesUserSerializer
    permission_classes = [IsAuthenticated, IsManager]

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "Foydalanuvchi muvaffaqiyatli yaratildi.",
            "user": {
                "id": user.id,
                "phone_number": user.phone_number,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "process": user.process.id if hasattr(user, "process") and user.process else None,
            }
        }, status=HTTP_201_CREATED)


@extend_schema(
    tags=["Manager Auth"],
    description="Manager uchun tizimga kirish.",
    request=LoginManagerUserSerializer,
    responses={200: None}
)
class LoginManagerUserAPIView(GenericAPIView):
    serializer_class = LoginManagerUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Muvaffaqiyatli kirish.",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "phone_number": user.phone_number,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "process": user.process.id if hasattr(user, "process") and user.process else None,
            }
        }, status=HTTP_200_OK)


@extend_schema(
    tags=["Manager Auth"],
    description="Manager tomonidan yangi foydalanuvchi yaratish.",
    request=ManagerCreatesUserSerializer,
)
class ManagerDestroyAPIView(DestroyAPIView):
    serializer_class = ManagerCreatesUserSerializer
    lookup_field = 'id'
