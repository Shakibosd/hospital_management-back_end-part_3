from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = models.Services.objects.all()
    serializer_class = serializers.ServicesSerializers