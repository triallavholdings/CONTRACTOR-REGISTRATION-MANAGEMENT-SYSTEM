from django.urls import include, path
from rest_framework import routers

from .views import (
    UserViewSet, GroupViewSet, CompanyDetailsViewSet,
    CompanySecretaryViewSet, BankerDetailsViewSet,
    AffiliatesViewSet, DirectorDetailsViewSet,
    ShareholderDetailsViewSet, EmployeesViewSet,
    VehicleEquipmentViewSet, ProjectsViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'companydetails', CompanyDetailsViewSet)
router.register(r'secretary', CompanySecretaryViewSet)
router.register(r'bankdetails', BankerDetailsViewSet)
router.register(r'affilites', AffiliatesViewSet)
router.register(r'directors', DirectorDetailsViewSet)
router.register(r'shareholders', ShareholderDetailsViewSet)
router.register(r'employees', EmployeesViewSet)
router.register(r'vehicleEquipment', VehicleEquipmentViewSet)
router.register(r'projects', ProjectsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
