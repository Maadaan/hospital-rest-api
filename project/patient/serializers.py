from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('patient_name','patient_email', 'patient_address','patient_phone_number','patient_doctor','patient_hospital')
