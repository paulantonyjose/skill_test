from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TableTwo
from .serializers import TableTwoSerializer

class TableTwoAPIView(APIView):
    def get(self, request,pk=None, *args, **kwargs):
        queryset = TableTwo.objects.all()
        if pk:
            queryset=queryset.filter(id=pk)
        serializer = TableTwoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TableTwoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            instance = TableTwo.objects.get(pk=request.POST.get('pk'))
        except TableTwo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TableTwoSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            instance = TableTwo.objects.get(pk=pk)
        except TableTwo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
