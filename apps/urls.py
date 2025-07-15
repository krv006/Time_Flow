from django.urls import path

from apps.views import UserListApiView

urlpatterns = [
    path('users/', UserListApiView.as_view(), name='users'),
]
