from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin


class CompanyAddress(SiteModelMixin, BaseUuidModel):

    cipa_id = models.CharField(
        verbose_name="Enter CIPA Unique Identification Number (UIN) Without BW",
        max_length=200)
    
    country = models.CharField(
        verbose_name="Country",
        max_length=200,)
    
    district = models.CharField(
        verbose_name="District",
        max_length=200)
    
    village_town = models.CharField(
        verbose_name="Village/Town/City",
        max_length=200)

    plot_unit = models.CharField(
        verbose_name="Plot/Unit No",
        max_length=10)

    street_ward = models.CharField(
        verbose_name="Street/Locality/Ward",
        max_length=200)

    postal = models.CharField(
        verbose_name="P.O.Bo or Private Bag",
        max_length=200,
        choices=(('p.o.box', 'P. O. Box'), ('private_bag', 'Private Bag')))

    box_number = models.CharField(
        verbose_name="Box Number",
        max_length=200)

    history = HistoricalRecords()
