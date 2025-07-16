from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.models import Process
from apps.serializers.product_serializer import ProcessModelSerializer


class ProcessListCreateAPIView(ListCreateAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessModelSerializer
    permission_classes = (AllowAny,)
