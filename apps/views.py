from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from apps.models import User
from apps.serializers import UserModelSerializer


@extend_schema(tags=["User"], description="User Get")
class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
