from django.db import models


class CompanyDetail(models.Model):
    
    local_provider = models.CharField(
        verbose_name="Are you a Local Provider/Contractor?",
        max_length=10,
        choices=(('Yes', 'yes'), ('No', 'no')))
    
    business_type = models.CharField(
        verbose_name="Business Type",
        max_length=200)
    
    name = models.CharField(
        verbose_name="Name of Company",
        max_length=200)

    cipa_registration = models.CharField(
        verbose_name="Are you Registered with CIPA?",
        max_length=10,
        choices=(('Yes', 'yes'), ('No', 'no')))

    cipa_id = models.CharField(
        verbose_name="Enter CIPA Unique Identification Number (UIN) Without BW",
        max_length=200)

    registration_date = models.DateTimeField("Date of Registration")

    ownership = models.CharField(
        verbose_name="Ownership",
        max_length=200)

    webpage = models.CharField(
        verbose_name="Webpage",
        max_length=200)
