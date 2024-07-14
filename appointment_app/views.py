from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class appointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.appointmentSerializers

    #custom query kortesi
    def get_queryset(self):
        queryset =  super().get_queryset() #7 no line ke niye aslam ba parent ke niye aslam
        patient_id = self.request.query_params.get('patient_id')   
        # print(self.request.query_params) 
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset