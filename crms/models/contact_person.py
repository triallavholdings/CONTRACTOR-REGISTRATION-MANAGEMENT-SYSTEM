from django.db import models


class ContactPerson(models.Model):

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

    email = models.CharField(
        verbose_name="Email",
        max_length=200)

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

    omang = models.CharField(
        verbose_name="Omang No",
        max_length=200)

    expiry_date = models.DateTimeField("Validity of Card")
  
    class Meta:
        abstract = True


class PrimaryContactPerson(ContactPerson):
    
    pass


class SecondaryContactPerson(ContactPerson):
    
    pass
