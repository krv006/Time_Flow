from django.urls import path

from apps.views import UserListApiView, RegisterAPIView, LoginAPIView

urlpatterns = [
    path('users/', UserListApiView.as_view(), name='users'),

    # todo Auth
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
