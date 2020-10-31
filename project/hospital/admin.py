from django.contrib import admin

from .models import Hospital, HospitalUrl, BloodBank

admin.site.register(Hospital)
admin.site.register(HospitalUrl)
admin.site.register(BloodBank)
