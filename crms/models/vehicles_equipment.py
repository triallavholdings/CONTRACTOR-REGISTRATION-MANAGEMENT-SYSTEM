from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin


class VehicleEquipment(SiteModelMixin, BaseUuidModel):
    
    asserts_value = models.CharField(
        verbose_name="Value of total of Company Assets in BWP:",
        max_length=200)

    equipment_value = models.CharField(
        verbose_name="Value of Equipment's (in BWP) (Plant, Equipment's but Excluding hire items)",
        max_length=200,)
    
    capital = models.CharField(
        verbose_name="Paid Up Capital (in BWP)",
        max_length=200)
    
    total_employees = models.CharField(
        verbose_name="Total Employeed",
        max_length=200)

    history = HistoricalRecords()


class Vehicle(SiteModelMixin, BaseUuidModel):
    
    vehicle_equipment = models.ForeignKey(
        VehicleEquipment, on_delete=models.CASCADE)

    registered_owner = models.CharField(
        verbose_name="Registered Owner",
        max_length=200,)
    
    ownership = models.CharField(
        verbose_name="Ownership",
        max_length=200,
        choices=(('Owned', 'owned'), ('Leased','Leased')))
    
    registration_no = models.CharField(
        verbose_name="Registration No",
        max_length=200)

    first_reg_date = models.DateTimeField(
        verbose_name="Date of First Registration")

    make_model = models.CharField(
        verbose_name="Vehicle Make/Model",
        max_length=200)

    prev_owner = models.CharField(
        verbose_name="Previous Owner",
        max_length=200)

    description = models.CharField(
        verbose_name="Description of Vehicle",
        max_length=200)
    
    present_value = models.DecimalField(
        verbose_name="Present Value (In BWP)",
        max_digits=10, decimal_places=2)

    attachments = models.FileField(
            verbose_name="Attachments e.g Ownership documents",
            upload_to ='uploads/% Y/% m/% d/')

    history = HistoricalRecords()


class PlantEquipment(SiteModelMixin, BaseUuidModel):
    
    vehicle_equipment = models.ForeignKey(
        VehicleEquipment, on_delete=models.CASCADE)

    owner_name = models.CharField(
        verbose_name="Name of the Owner",
        max_length=200,)
    
    ownership = models.CharField(
        verbose_name="Ownership",
        max_length=200,
        choices=(('Owned', 'owned'), ('Leased','Leased')))
    
    registration_no = models.CharField(
        verbose_name="Registration No",
        max_length=200)

    date_of_purchase = models.DateTimeField(
        verbose_name="Date of Purchase")

    description = models.CharField(
        verbose_name="Description of Vehicle",
        max_length=200)
    
    present_value = models.DecimalField(
        verbose_name="Present Value (In BWP)",
        max_digits=10, decimal_places=2)

    attachments = models.FileField(
            verbose_name="Attachments e.g Plant Equipment documents",
            upload_to ='uploads/% Y/% m/% d/')

    history = HistoricalRecords()


class OfficeEquipments(SiteModelMixin, BaseUuidModel):
    
    vehicle_equipment = models.ForeignKey(
        VehicleEquipment, on_delete=models.CASCADE)

    office_furniture = models.CharField(
        verbose_name="Office Furniture",
        max_length=200,)
    
    present_value = models.DecimalField(
        verbose_name="Present Value (In BWP)",
        max_digits=10, decimal_places=2)

    attachments = models.FileField(
            verbose_name="Attachments e.g Affiliation documents",
            upload_to ='uploads/% Y/% m/% d/')

    history = HistoricalRecords()
