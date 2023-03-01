from django.urls import path, include
from .views import TableTwoAPIView


urlpatterns = [
    path('tabletwo/', TableTwoAPIView.as_view(), name='tabletwo_list_create'),
    path('tabletwo/<int:pk>/', TableTwoAPIView.as_view(), name='tabletwo_detail'),
]