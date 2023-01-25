from rest_framework import serializers
from .models import ScheduleEvent



class SchedulEvenSerializer (serializers.ModelSerializer):
    class Meta :
        model = ScheduleEvent
        
