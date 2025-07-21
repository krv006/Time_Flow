from django.urls import path

from apps.views import UserListApiView, RegisterAPIView, LoginAPIView, ProcessListCreateAPIView, \
    ProductListCreateAPIView, ManagerLoginAPIView, ManagerCreatesUserView

urlpatterns = [
    path('users/', UserListApiView.as_view(), name='users'),

    # todo Auth
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),

    # todo Manager
    path('process/', ProcessListCreateAPIView.as_view(), name='process'),
    path('product/', ProductListCreateAPIView.as_view(), name='product'),
    path('manager-register/', ManagerCreatesUserView.as_view(), name='manager-register'),
    path('manager-login/', ManagerLoginAPIView.as_view(), name='manager-login'),

]
