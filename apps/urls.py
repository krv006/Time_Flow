from django.urls import path

from apps.views import UserListApiView, RegisterAPIView, LoginAPIView, ProcessListCreateAPIView, \
    ProductListCreateAPIView, LoginManagerUserAPIView, ManagerCreatesUserView, MaterialListCreateAPIView, \
    ProcessingListCreateAPIView, ManagerDestroyAPIView, ProductDestroyAPIView, ProcessDestroyAPIView

urlpatterns = [
    path('users/', UserListApiView.as_view(), name='users'),

    # todo Auth
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),

    # todo Manager
    path('process/', ProcessListCreateAPIView.as_view(), name='process'),
    path('process-delete/<int:pk>', ProcessDestroyAPIView.as_view(), name='process-delete'),
    path('product/', ProductListCreateAPIView.as_view(), name='product'),
    path('product-delete/<int:pk>', ProductDestroyAPIView.as_view(), name='product-delete'),
    path('manager-register/', ManagerCreatesUserView.as_view(), name='manager-register'),
    path('manager-delete/<int:pk>', ManagerDestroyAPIView.as_view(), name='manager-user-delete'),
    path('manager-login/', LoginManagerUserAPIView.as_view(), name='manager-login'),

    # todo Warehouseman
    path('material/', MaterialListCreateAPIView.as_view(), name='material'),
    path('processing/', ProcessingListCreateAPIView.as_view(), name='processing'),
]
