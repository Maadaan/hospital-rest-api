from django.db import models
from hospital.models import Hospital


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=200)
    doctor_address = models.CharField(max_length=200)
    doctor_email = models.EmailField()
    doctor_phone_number = models.CharField(max_length=20)
    doctor_working_hospital = models.ManyToManyField(
        Hospital)

    def __str__(self):
        return self.doctor_name
