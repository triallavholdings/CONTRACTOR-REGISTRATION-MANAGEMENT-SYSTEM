from django.db import models


class Directors(models.Model):
    
    cipa_id = models.CharField(
        verbose_name="Enter CIPA Unique Identification Number (UIN) Without BW",
        max_length=200)

class DirectorDetails(models.Model):
    
    directors = models.ForeignKey(Directors, on_delete=models.CASCADE)

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

    omang = models.CharField(
        verbose_name="Omang No",
        max_length=200)

    expiry_date = models.DateTimeField("Validity of Card")

    passport_number = models.CharField(
        verbose_name="Passport Number",
        max_length=200)

    work_permit = models.CharField(
        verbose_name="Work Permit",
        max_length=200)

    email = models.CharField(
        verbose_name="Email",
        max_length=200)

    attachments = models.FileField(
            verbose_name="Attachments e.g Affiliation documents",
            upload_to ='uploads/% Y/% m/% d/')