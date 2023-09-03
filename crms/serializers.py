from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import (
    CompanyDetail,  BankerDetails, Affiliates, DirectorDetails,
    ShareholderDetails, Employees, VehicleEquipment, Projects,
    CompanySecretary)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CompanyDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyDetail
        fields = '__all__'
        

class BankerDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankerDetails
        fields = '__all__'


class AffiliatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Affiliates
        fields = '__all__'
        

class DirectorDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DirectorDetails
        fields = '__all__'


class ShareholderDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShareholderDetails
        fields = '__all__'


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class VehicleEquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleEquipment
        fields = '__all__'


class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class CompanySecretarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanySecretary
        fields = '__all__'
