from django.urls import path
from .views import TokenAPIView

urlpatterns = [
    path('auth/', TokenAPIView.as_view(), name='token-auth'),
]