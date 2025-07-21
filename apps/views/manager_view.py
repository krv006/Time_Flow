from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
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
    description="Manager foydalanuvchini tizimga kiritish (login).",
    request=LoginManagerUserSerializer,
)
class ManagerLoginAPIView(GenericAPIView):
    queryset = ManagerUser.objects.all()
    serializer_class = LoginManagerUserSerializer
    permission_classes = (IsManager,)

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
