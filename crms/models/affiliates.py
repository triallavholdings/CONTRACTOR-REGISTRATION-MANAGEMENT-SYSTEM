from django.db import models


class Affiliates(models.Model):
    
    affiliate = models.CharField(
        verbose_name="Name and group of the Affiliated Firm",
        max_length=200)
    
    address = models.CharField(
        verbose_name="Address",
        max_length=200)

    attachments = models.FileField(
        verbose_name="Attachments e.g Affiliation documents",
        upload_to ='uploads/% Y/% m/% d/')