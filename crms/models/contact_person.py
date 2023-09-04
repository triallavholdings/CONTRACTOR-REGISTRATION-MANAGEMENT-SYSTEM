from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin

from django_crypto_fields.fields import IdentityField


class ContactPerson(SiteModelMixin, BaseUuidModel):

    cipa_id = models.CharField(
        verbose_name="Enter CIPA Unique Identification Number (UIN) Without BW",
        max_length=200)

    first_name = models.CharField(
        verbose_name="First Name",
        max_length=200,)
    
    middle_name = models.CharField(
        verbose_name="Middle Name",
        max_length=200)
    
    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=200)

    dob = models.DateTimeField("Date of Birth")

    email = models.EmailField(
        verbose_name="Email")

    cell_phone = models.CharField(
        verbose_name="Cell Phone no",
        max_length=200)
    
    tel_phone = models.CharField(
        verbose_name="Telephone Phone no",
        max_length=200)

    business_phone = models.CharField(
        verbose_name="Business Phone no",
        max_length=200)

    nationality = models.CharField(
        verbose_name="Nationality",
        max_length=200)

    omang = IdentityField()

    expiry_date = models.DateTimeField("Validity of Card")
  
    class Meta:
        abstract = True


class PrimaryContactPerson(ContactPerson):
    
    history = HistoricalRecords()


class SecondaryContactPerson(ContactPerson):
    
    history = HistoricalRecords()
