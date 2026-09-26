from django.db import models

class Network(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    governorate_ar = models.CharField(default='N/A',max_length=100, verbose_name='المحافظة')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    area_ar = models.CharField(default='N/A',max_length=100, null=True, verbose_name='المنطقة')
    type = models.CharField(max_length=100, verbose_name='Type')
    type_ar = models.CharField(default='N/A',max_length=100, verbose_name='النوع')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    speciality_ar = models.CharField(default='N/A',max_length=255, verbose_name='التخصص')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    provider_ar = models.CharField(default='N/A',max_length=255, verbose_name='مقدم الخدمة')
    discount = models.CharField(max_length=50, blank=True, null=True, verbose_name='Discount')
    address = models.TextField(verbose_name='Address')
    address_ar = models.TextField(default='N/A', verbose_name='العنوان')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"


class Networkedsnew(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    governorate_ar = models.CharField(default='N/A',max_length=100, verbose_name='المحافظة')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    area_ar = models.CharField(default='N/A',max_length=100, null=True, verbose_name='المنطقة')
    type = models.CharField(max_length=100, verbose_name='Type')
    type_ar = models.CharField(default='N/A',max_length=100, verbose_name='النوع')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    speciality_ar = models.CharField(default='N/A',max_length=255, verbose_name='التخصص')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    provider_ar = models.CharField(default='N/A',max_length=255, verbose_name='مقدم الخدمة')
    address = models.TextField(default='N/A',verbose_name='Address')
    address_ar = models.TextField(default='N/A', verbose_name='العنوان')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"

class Networkmofa(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    governorate_ar = models.CharField(default='N/A',max_length=100, verbose_name='المحافظة')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    area_ar = models.CharField(default='N/A',max_length=100, null=True, verbose_name='المنطقة')
    type = models.CharField(max_length=100, verbose_name='Type')
    type_ar = models.CharField(default='N/A',max_length=100, verbose_name='النوع')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    speciality_ar = models.CharField(default='N/A',max_length=255, verbose_name='التخصص')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    provider_ar = models.CharField(default='N/A',max_length=255, verbose_name='مقدم الخدمة')
    address = models.TextField(default="N/A",verbose_name='Address')
    address_ar = models.TextField(default='N/A', verbose_name='العنوان')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"

class Networkexxon(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    governorate_ar = models.CharField(default='N/A',max_length=100, verbose_name='المحافظة')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    area_ar = models.CharField(default='N/A',max_length=100, null=True, verbose_name='المنطقة')
    type = models.CharField(max_length=100, verbose_name='Type')
    type_ar = models.CharField(default='N/A',max_length=100, verbose_name='النوع')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    speciality_ar = models.CharField(default='N/A',max_length=255, verbose_name='التخصص')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    provider_ar = models.CharField(default='N/A',max_length=255, verbose_name='مقدم الخدمة')
    address = models.TextField(default="N/A",verbose_name='Address')
    address_ar = models.TextField(default='N/A', verbose_name='العنوان')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"

class Networkemfa(models.Model):
    # --- Country ---
    country = models.CharField(blank=True, null=True,max_length=100, default='Egypt', verbose_name='Country')
    country_ar = models.CharField(blank=True, null=True,default='مصر', max_length=100, verbose_name='الدولة')

    # --- City (replaces governorate) ---
    city = models.CharField(blank=True, null=True,max_length=100, verbose_name='City')
    city_ar = models.CharField(blank=True, null=True,default='N/A', max_length=100, verbose_name='المدينة')

    # --- Health provider ---
    provider = models.CharField(blank=True, null=True,max_length=255, verbose_name='Health Provider')
    provider_ar = models.CharField(blank=True, null=True,default='N/A', max_length=255, verbose_name='مقدم الخدمة')

    # --- Address ---
    address = models.TextField(blank=True, null=True,default='N/A', verbose_name='Address')
    address_ar = models.TextField(blank=True, null=True,default='N/A', verbose_name='العنوان')

    # --- Type ---
    type = models.CharField(blank=True, null=True,max_length=100, verbose_name='Type')
    type_ar = models.CharField(blank=True, null=True,default='N/A', max_length=100, verbose_name='النوع')

    # --- Specialty(ies) ---
    speciality = models.TextField(blank=True, null=True,verbose_name='Specialty(ies)')
    speciality_ar = models.TextField(blank=True, null=True,default='N/A', verbose_name='التخصص(ات)')

    # --- Contact ---
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='Phone')
    mobile = models.CharField(max_length=100, blank=True, null=True, verbose_name='Mobile')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    website = models.URLField(blank=True, null=True, verbose_name='Website')

    # --- Comment ---
    notes = models.TextField(blank=True, null=True, verbose_name='Comment')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.city}"


class Networkhorizon(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    governorate_ar = models.CharField(default='N/A',max_length=100, verbose_name='المحافظة')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    area_ar = models.CharField(default='N/A',max_length=100, null=True, verbose_name='المنطقة')
    type = models.CharField(max_length=100, verbose_name='Type')
    type_ar = models.CharField(default='N/A',max_length=100, verbose_name='النوع')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    speciality_ar = models.CharField(default='N/A',max_length=255, verbose_name='التخصص')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    provider_ar = models.CharField(default='N/A',max_length=255, verbose_name='مقدم الخدمة')
    address = models.TextField(default="N/A",verbose_name='Address')
    address_ar = models.TextField(default='N/A', verbose_name='العنوان')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"




class NetworkHorizonGlobal(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    governorate_ar = models.CharField(default='N/A',max_length=100, verbose_name='المحافظة')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    area_ar = models.CharField(default='N/A',max_length=100, null=True, verbose_name='المنطقة')
    type = models.CharField(max_length=100, verbose_name='Type')
    type_ar = models.CharField(default='N/A',max_length=100, verbose_name='النوع')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    speciality_ar = models.CharField(default='N/A',max_length=255, verbose_name='التخصص')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    provider_ar = models.CharField(default='N/A',max_length=255, verbose_name='مقدم الخدمة')
    discount = models.CharField(max_length=50, blank=True, null=True, verbose_name='Discount')
    address = models.TextField(verbose_name='Address')
    address_ar = models.TextField(default='N/A', verbose_name='العنوان')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"