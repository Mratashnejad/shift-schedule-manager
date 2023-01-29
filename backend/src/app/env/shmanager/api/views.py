from django.shortcuts import render

# Create your views here.
from rest_framework import viewset
from .models import ScheduleEvent
from .serializer import SchedulEventSerializer

class SchedulEventViewSet (viewsets.ModelViewSet):
    queryset = ScheduleEvent.objects.all()
    serializer_class = SchedulEventSerializer

    


