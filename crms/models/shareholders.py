from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin

from django_crypto_fields.fields import IdentityField


class Shareholders(SiteModelMixin, BaseUuidModel):
    
    cipa_id = models.CharField(
        verbose_name="Enter CIPA Unique Identification Number (UIN) Without BW",
        max_length=200)

    history = HistoricalRecords()

class ShareholderDetails(SiteModelMixin, BaseUuidModel):
    
    shareholders = models.ForeignKey(Shareholders, on_delete=models.CASCADE)

    first_name = models.CharField(
        verbose_name="First Name",
        max_length=200,)
    
    middle_name = models.CharField(
        verbose_name="Middle Name",
        max_length=200)
    
    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=200)

    gender = models.CharField(
        verbose_name="Gender",
        max_length=200)

    dob = models.DateTimeField("Date of Birth")

    nationality = models.CharField(
        verbose_name="Nationality",
        max_length=200)

    omang = IdentityField(
        verbose_name="Omang No")

    expiry_date = models.DateTimeField("Validity of Card")

    passport_number = models.CharField(
        verbose_name="Passport Number",
        max_length=200)

    work_permit = models.CharField(
        verbose_name="Work Permit",
        max_length=200)

    percentage_shares = models.CharField(
        verbose_name="Percentage of Shares",
        max_length=200)

    gov_employee = models.CharField(
        verbose_name="Government Employee",
        max_length=200,
        choices=(('yes', 'Yes'), ('no', 'No')))

    email = models.CharField(
        verbose_name="Email",
        max_length=200)

    attachments = models.FileField(
            verbose_name="Attachments e.g Affiliation documents",
            upload_to ='uploads/% Y/% m/% d/')

    history = HistoricalRecords()
