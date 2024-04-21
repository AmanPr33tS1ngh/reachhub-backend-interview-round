from django.shortcuts import render
from rest_framework.views import APIView
from .models import Ingestion
from .serializers import IngestionSerializer
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Q

# Create your views here.

class IngestionAPI(APIView):
    def get(self, request, *args, **kwargs):
        # try:
        level = request.GET.get('level')
        userId = request.GET.get('userId')
        startTime = request.GET.get('startTime')
        endTime = request.GET.get('endTime')
        
        query = Q()
        if level:
            query &= Q(level=level)
        if userId:
            query &= Q(userId=userId)
        if startTime and endTime:
            query &= Q(timestamp__range=(startTime, endTime))
            
        logs = Ingestion.objects.filter(
            query
        )
        
        return JsonResponse({'logs': IngestionSerializer(logs, many=True).data})
        # except Exception as e:
        #     pass
        
    def post(self, request, *args, **kwargs):
        try:
            level = request.data.get('level')
            message = request.data.get('message')
            userId = int(request.data.get('userId'))        
            timestamp = request.data.get('timestamp')
            formatted_timestamp = datetime.fromisoformat(timestamp)
            
            Ingestion.objects.create(
                level=level,
                message=message,
                userId=userId,
                timestamp=formatted_timestamp,
            )
            
            return JsonResponse({}, status=201)
        except Exception as e:
            return JsonResponse({'err': str(e)}, status=400)