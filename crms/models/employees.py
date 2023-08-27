from django.db import models


class Employees(models.Model):
    
    cipa_id = models.CharField(
        verbose_name="Enter CIPA Unique Identification Number (UIN) Without BW",
        max_length=200)

    bw_employees = models.CharField(
        verbose_name="Total Number of Botswana Citizens",
        max_length=200,)
    
    other_nationalities = models.CharField(
        verbose_name="TOtal Number of Other Nationalities",
        max_length=200)
    
    total_employees = models.CharField(
        verbose_name="Total Employeed",
        max_length=200)

class SeniorPermenantStaffBW(models.Model):
    
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE)

    first_name = models.CharField(
        verbose_name="First Name",
        max_length=200,)
    
    middle_name = models.CharField(
        verbose_name="Middle Name",
        max_length=200)
    
    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=200)

    omang = models.CharField(
        verbose_name="Omang No",
        max_length=200)

    dob = models.DateTimeField("Date of Birth")

    profession_trade = models.CharField(
        verbose_name="Profession/Trade",
        max_length=200)

    position = models.CharField(
        verbose_name="Position in Firm",
        max_length=200)

    qualification = models.CharField(
        verbose_name="Qualification",
        max_length=200)

    attachments = models.FileField(
            verbose_name="Attachments e.g Affiliation documents",
            upload_to ='uploads/% Y/% m/% d/')


class SeniorPermenantStaffForeigner(models.Model):
    
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE)

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

    passport_number = models.CharField(
        verbose_name="Passport Number",
        max_length=200)

    work_permit = models.CharField(
        verbose_name="Work Permit Number",
        max_length=200)

    expiry_date = models.DateTimeField("Validity of Permit")

    profession_trade = models.CharField(
        verbose_name="Profession/Trade",
        max_length=200)

    position = models.CharField(
        verbose_name="Position in Firm",
        max_length=200)

    qualification = models.CharField(
        verbose_name="Qualification",
        max_length=200)

    attachments = models.FileField(
            verbose_name="Attachments e.g Affiliation documents",
            upload_to ='uploads/% Y/% m/% d/')
