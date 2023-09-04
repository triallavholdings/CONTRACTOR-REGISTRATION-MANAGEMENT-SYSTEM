from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin

LOCALITY = (
    ('bobonong', 'Bobonong'),
    ('bokaa', 'Bokaa'),
    ('borolong', 'Borolong'),
    ('chadibe', 'Chadibe'),
    ('dukwi', 'Dukwi'))


class Projects(SiteModelMixin, BaseUuidModel):

    cipa_id = models.CharField(
        verbose_name="Enter CIPA Unique Identification Number (UIN) Without BW",
        max_length=200)
    
    history = HistoricalRecords()


class CompletedProject(SiteModelMixin, BaseUuidModel):
    
    projects = models.ForeignKey(
        Projects, on_delete=models.CASCADE)

    name = models.CharField(
        verbose_name="Project name",
        max_length=200,)
    
    details = models.CharField(
        verbose_name="Project Details",
        max_length=200)
    
    client = models.CharField(
        verbose_name="Client",
        max_length=200)

    client_representation = models.DateTimeField(
        verbose_name="Client Representation")

    contact_number = models.CharField(
        verbose_name="Client contact number",
        max_length=200)
    
    date_completed = models.DateField(
        verbose_name="Date Completed")

    locality = models.CharField(
        verbose_name="Locality",
        max_length=200,
        choices=LOCALITY)

    contract_value = models.DecimalField(
        verbose_name="Value of Contract (In BWP)",
        max_digits=10, decimal_places=2)

    attachments = models.FileField(
            verbose_name="Attachments e.g Project documents",
            upload_to ='uploads/% Y/% m/% d/')

    history = HistoricalRecords()


class OnGoingProject(models.Model):
    
    projects = models.ForeignKey(
        Projects, on_delete=models.CASCADE)

    name = models.CharField(
        verbose_name="Project name",
        max_length=200,)
    
    details = models.CharField(
        verbose_name="Project Details",
        max_length=200)
    
    client = models.CharField(
        verbose_name="Client",
        max_length=200)

    client_representation = models.DateTimeField(
        verbose_name="Client Representation")

    contact_number = models.CharField(
        verbose_name="Client contact number",
        max_length=200)
    
    date_started = models.DateField(
        verbose_name="Date Started")

    locality = models.CharField(
        verbose_name="Locality",
        max_length=200,
        choices=LOCALITY)

    contract_value = models.DecimalField(
        verbose_name="Value of Contract (In BWP)",
        max_digits=10, decimal_places=2)

    attachments = models.FileField(
            verbose_name="Attachments e.g Project documents",
            upload_to ='uploads/% Y/% m/% d/')

    history = HistoricalRecords()
