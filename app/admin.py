from django.contrib import admin
from .models import Network,Networkedsnew,Networkemfa,Networkmofa,Networkexxon,Networkhorizon,NetworkHorizonGlobal
from import_export.admin import ImportExportModelAdmin
from django.db import models

@admin.register(Network)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone','discount']
    list_display_links = ['provider', 'phone','discount']
    search_fields = ['governorate','area','type','speciality','provider','address','phone','discount']
    list_filter = ['provider','governorate','area','discount']


@admin.register(Networkedsnew)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']



@admin.register(Networkmofa)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']

@admin.register(Networkexxon)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']

# ==========================================================
# admin.py -> Networkemfa
# استبدل الكلاس القديم بده بالكامل
# ==========================================================



@admin.register(Networkhorizon)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']


@admin.register(NetworkHorizonGlobal)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']



from import_export import resources

# ==========================================================
# Networkemfa (المودل الجديد: country/city بدل governorate/area)
# ==========================================================

class NetworkemfaResource(resources.ModelResource):
    class Meta:
        model = Networkemfa
        fields = (
            'id',
            'country', 'country_ar',
            'city', 'city_ar',
            'type', 'type_ar',
            'speciality', 'speciality_ar',
            'provider', 'provider_ar',
            'address', 'address_ar',
            'phone', 'mobile', 'email', 'website', 'notes',
        )
        export_order = fields


@admin.register(Networkemfa)
class NetworkemfaAdmin(ImportExportModelAdmin):
    resource_class = NetworkemfaResource
    list_display = ['provider', 'country', 'city', 'type', 'phone', 'mobile', 'email']
    list_display_links = ['provider', 'phone']
    search_fields = ['provider', 'provider_ar', 'city', 'city_ar', 'address', 'address_ar', 'speciality', 'phone', 'mobile', 'email']
    list_filter = ['country', 'city', 'type']