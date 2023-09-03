from django.db import models


class CompanySecretary(models.Model):
    
    name = models.CharField(
        verbose_name="Name",
        max_length=10)
    
    home_phone = models.CharField(
        verbose_name="Home Phone No.:",
        max_length=200)
    
    bus_phone = models.CharField(
        verbose_name="usiness Phone no.:",
        max_length=200)

    mobile_no = models.CharField(
        verbose_name="Mobile no.:",
        max_length=10)

    email = models.EmailField(
        verbose_name="Email:")

    nationality = models.CharField(
        verbose_name="Nationality",
        max_length=200)

    omang = models.CharField(
        verbose_name="Omang No.:",
        max_length=200)
    
    expiry_date = models.DateTimeField("Expiry Date:")


class PhysicalAddress(models.Model):
    
    secretary = models.ForeignKey(CompanySecretary, on_delete=models.CASCADE)

    plot = models.CharField(
        verbose_name="Plot/Unit No.:",
        max_length=200,)
    
    street = models.CharField(
        verbose_name="Street:",
        max_length=200)
    
    village_town_city = models.CharField(
        verbose_name="Village/Town/City :",
        max_length=200)


class PostalAddress(models.Model):
    
    secretary = models.ForeignKey(CompanySecretary, on_delete=models.CASCADE)

    box_private_no = models.CharField(
        verbose_name="P.O.Box / Private Bag:",
        max_length=200,)
    
    number = models.CharField(
        verbose_name="No.::",
        max_length=200)
    
    address_line = models.CharField(
        verbose_name="Line Address 1:",
        max_length=200)

    address_line2 = models.CharField(
        verbose_name="Line Address 2:",
        max_length=200)
    
    address_line3 = models.CharField(
        verbose_name="Line Address 3:",
        max_length=200)
    
    country = models.CharField(
        verbose_name="Country:",
        max_length=200)

    village_town_city = models.CharField(
        verbose_name="Village/Town/City :",
        max_length=200)
