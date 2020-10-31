from django.db import models
from doctor.models import Doctor
from hospital.models import Hospital


class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    patient_address = models.CharField(max_length=100)
    patient_phone_number = models.CharField(max_length=20)
    patient_doctor = models.ManyToManyField(Doctor)
    patient_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name
