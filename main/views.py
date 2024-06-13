from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Request
from .serializers import RequestSerializer
import time
import random


class QueryView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            req = Request.objects.get(pk=request.data['id'])
            # time.sleep(random.uniform(0, 60))  # Эмуляция задержки до 60 секунд
            result = random.choice([True, False])
            req.result = result
            req.save()
            return Response({'result': result}, status=status.HTTP_200_OK)
        except Request.DoesNotExist:
            return Response({'error': 'Request not found'}, status=status.HTTP_404_NOT_FOUND)


class HistoryView(generics.ListAPIView):
    serializer_class = RequestSerializer

    def get_queryset(self):
        cadastral_number = self.request.query_params.get('cadastral_number')
        if cadastral_number:
            return Request.objects.filter(cadastral_number=cadastral_number)
        return Request.objects.all()


class PingView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
