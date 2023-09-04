from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin


class Affiliates(SiteModelMixin, BaseUuidModel):
    
    affiliate = models.CharField(
        verbose_name="Name and group of the Affiliated Firm",
        max_length=200)
    
    address = models.CharField(
        verbose_name="Address",
        max_length=200)

    attachments = models.FileField(
        verbose_name="Attachments e.g Affiliation documents",
        upload_to ='uploads/% Y/% m/% d/')

    history = HistoricalRecords()

    def __str__(self):
        return self.affiliate