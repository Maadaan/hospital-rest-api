from django.db import models

blood_types = (
    ('O+', 'O-Positive'), ('O-', 'O-Negative'), ('A+', 'A-Positive'),
    ('A-', 'A-Negative'), ('B+', 'B-Positive'),
    ('B-', 'B-Negative'), ('AB+', 'AB-Positive'), ('AB-', 'AB-Negative'))


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    hospital_email = models.EmailField()
    hospital_address = models.CharField(max_length=100)
    hospital_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.hospital_name


class HospitalUrl(models.Model):
    hospital_url = models.OneToOneField(Hospital, on_delete=models.CASCADE)
    facebook_url = models.CharField(max_length=100)
    instagram_url = models.CharField(max_length=100)


class BloodBank(models.Model):
    blood_hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
    blood_types = models.CharField(max_length=5, choices=blood_types)
