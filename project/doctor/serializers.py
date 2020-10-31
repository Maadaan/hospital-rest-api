from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('doctor_name','doctor_address', 'doctor_email','doctor_phone_number','doctor_working_hospital' )
