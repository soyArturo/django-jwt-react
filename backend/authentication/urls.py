from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView, )
from .views import ObtainTokenPairWithColorView, CustomUserCreate

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
