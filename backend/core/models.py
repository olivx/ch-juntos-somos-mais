from django.contrib.gis.db import models

# Create your models here.
class Customer(models.Model):
    MALE = "M"
    FEMALE = "F"
    GENDER_OPTION = (("FEMALE", FEMALE), ("MALE", MALE))

    name_title = models.CharField(max_length=200)
    name_first = models.CharField(max_length=200)
    name_last = models.CharField(max_length=200)
    gender = models.CharField(max_lenth=1, choice=GENDER_OPTION)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    nationality = models.CharField(max_length=2)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name_title


class MobileNumbers(models.Model):
    customer = models.OneToOneField(Customer, on_delete=True)
    mobile_numbers = models.CharField(max_length=15)

    def __str__(self):
        return self.mobile_numbers


class TelephoneNumbers(models.Model):
    customer = models.OneToOneField(Customer, on_delete=True)
    telephone_numbers = models.CharField(max_length=15)

    def __str__(self):
        return self.telephone_numbers


class Picture(models.Model):
    customer = models.OneToOneField(Customer, on_delete=True)
    large = models.ImageField()
    medium = models.ImageField()
    thumbnail = models.ImageField()


class Location(models.Model):
    street = models.CharField(max_legth=200)
    city = models.CharField(max_legth=100)
    state = models.CharField(max_legth=100)
    postcode = models.CharField(max_legth=50)
    region = models.CharField(max_legth=50)
    coordinates = models.PointField()
    timezone = models.CharField(max_legth=20)

    def __str__(self):
        return self.street
