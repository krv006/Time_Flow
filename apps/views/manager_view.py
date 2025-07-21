from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework_simplejwt.tokens import RefreshToken

from apps.models import ManagerUser
from apps.permission import IsManager
from apps.serializers import ManagerCreatesUserSerializer, LoginManagerUserSerializer


@extend_schema(
    tags=["Manager Auth"],
    description="Manager tomonidan yangi foydalanuvchi yaratish.",
    request=ManagerCreatesUserSerializer,
    responses={201: ManagerCreatesUserSerializer}
)
class ManagerCreatesUserView(CreateAPIView):
    queryset = ManagerUser.objects.all()
    serializer_class = ManagerCreatesUserSerializer
    permission_classes = [IsAuthenticated, IsManager]

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        manager = serializer.save()
        return Response({
            "message": "Foydalanuvchi muvaffaqiyatli yaratildi.",
            "manager": {
                "id": manager.id,
                "phone_number": manager.phone_number,
                "name": manager.name,
                "process": manager.process.id if manager.process else None,
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
                "name": user.name,
                "process": user.process.id if user.process else None,
            }
        }, status=HTTP_200_OK)
