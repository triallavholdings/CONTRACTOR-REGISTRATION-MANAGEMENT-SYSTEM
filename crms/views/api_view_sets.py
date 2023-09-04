from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from ..serializers import (
    UserSerializer, GroupSerializer, CompanyDetailsSerializer,
    BankerDetailsSerializer, AffiliatesSerializer,
    DirectorDetailsSerializer, ShareholderDetailsSerializer,
    EmployeesSerializer, VehicleEquipmentSerializer,
    ProjectsSerializer, CompanySecretarySerializer)
from ..models import (
    CompanyDetail,  BankerDetails, Affiliates, DirectorDetails,
    ShareholderDetails, Employees, VehicleEquipment, Projects,
    CompanySecretary)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyDetailsViewSet(viewsets.ModelViewSet):

    queryset = CompanyDetail.objects.all()
    serializer_class = CompanyDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]


class BankerDetailsViewSet(viewsets.ModelViewSet):

    queryset = BankerDetails.objects.all()
    serializer_class = BankerDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]


class AffiliatesViewSet(viewsets.ModelViewSet):

    queryset = Affiliates.objects.all()
    serializer_class = AffiliatesSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'affiliate'


class DirectorDetailsViewSet(viewsets.ModelViewSet):

    queryset = DirectorDetails.objects.all()
    serializer_class = DirectorDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class ShareholderDetailsViewSet(viewsets.ModelViewSet):

    queryset = ShareholderDetails.objects.all()
    serializer_class = ShareholderDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]



class EmployeesViewSet(viewsets.ModelViewSet):

    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [permissions.IsAuthenticated]


class VehicleEquipmentViewSet(viewsets.ModelViewSet):

    queryset = VehicleEquipment.objects.all()
    serializer_class = VehicleEquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]



class ProjectsViewSet(viewsets.ModelViewSet):

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanySecretaryViewSet(viewsets.ModelViewSet):

    queryset = CompanySecretary.objects.all()
    serializer_class = CompanySecretarySerializer
    permission_classes = [permissions.IsAuthenticated]
