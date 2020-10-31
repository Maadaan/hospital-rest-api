from django.urls import include, path
from rest_framework import routers

from . import views

# from doctor.views import Doctor
# from patient.views import Patient
# from .views import Hospital, HospitalUrl, BloodBank



from django.urls import include ,path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'hospitals', views.HospitalViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
