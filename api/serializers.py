from rest_framework import serializers
from .models import Ingestion

class IngestionSerializer(serializers.Serializer):
    timestamp = serializers.SerializerMethodField()
    userId = serializers.SerializerMethodField()
    message = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    
    def get_timestamp(self, obj):
        return obj.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
    def get_userId(self, obj):
        return obj.userId
        
    def get_message(self, obj):
        return obj.message
        
    def get_level(self, obj):
        return obj.level
        
    class Meta:
        model = Ingestion
        fields = ('timestamp', 'id', 'userId', 'message', 'level')
