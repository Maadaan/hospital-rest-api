from django.shortcuts import render

from rest_framework import viewsets
from .serializers import HospitalSerializer, HospitalUrlSerializer, BloodBankSerializer
from .models import Hospital, HospitalUrl, BloodBank


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all().order_by('id')
    serializer_class = HospitalSerializer


class HospitalUrlViewSet(viewsets.ModelViewSet):
    queryset = HospitalUrl.objects.all()
    serializer_class = HospitalUrlSerializer


class BloodBankViewSet(viewsets.ModelViewSet):
    queryset = BloodBank.objects.all()
    serializer_class = BloodBankSerializer
