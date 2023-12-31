from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin


class BankerDetails(SiteModelMixin, BaseUuidModel):
    
    bank_name = models.CharField(
        verbose_name="Name of Bank",
        max_length=200)
    
    branch = models.CharField(
        verbose_name="Branch Name",
        max_length=200)
    
    branch_code = models.CharField(
        verbose_name="Branch Code",
        max_length=200)

    account = models.CharField(
        verbose_name="Account Number",
        max_length=200,)

    account_type = models.CharField(
        verbose_name="Account Type",
        max_length=200)

    swift_code = models.CharField(
        verbose_name="Swift Code",
        max_length=200)

    attachments = models.FileField(
        verbose_name="Attachments e.g Bank confirmation letter",
        upload_to ='uploads/% Y/% m/% d/')

    history = HistoricalRecords()