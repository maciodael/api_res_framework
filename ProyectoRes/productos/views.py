from django.shortcuts import render
from rest_framework import viewsets
from .models import Jugo
from .serializers import JugoSerializer

class JugoViewSet(viewsets.ModelViewSet):
    serializer_class = JugoSerializer
    queryset = Jugo.objects.all()