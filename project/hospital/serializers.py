from rest_framework import serializers
from .models import Hospital, HospitalUrl, BloodBank


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields = ('hospital_name', 'hospital_email', 'hospital_address','hospital_phone_number')


class HospitalUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HospitalUrl
        fields = ('hospital_url','facebook_url', 'instagram_url')


class BloodBankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BloodBank
        fields = ('blood_hospital', 'blood_types')
