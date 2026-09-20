from django.db import models

# Create your models here.

class Networkar(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    discount = models.CharField(max_length=50, blank=True, null=True, verbose_name='Discount')
    address = models.TextField(null=True,verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"


class Networkedsar(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100, null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"


class Networkmofaar(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100, null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"


class Networkexxonar(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100, null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"


class Networkemfaar(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100, null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"

class Networkhorizonar(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100, null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"