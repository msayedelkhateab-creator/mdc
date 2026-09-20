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

@admin.register(Networkemfa)
class NetworkEmfaAdmin(ImportExportModelAdmin):
    list_display = [
        'country', 'governorate', 'area', 'type',
        'speciality', 'provider', 'phone', 'address_short',
    ]
    list_display_links = ['provider']
    list_editable = ['phone']

    search_fields = [
        'country', 'country_ar',
        'governorate', 'governorate_ar',
        'area', 'area_ar',
        'type', 'type_ar',
        'speciality', 'speciality_ar',
        'provider', 'provider_ar',
        'address', 'address_ar',
        'phone', 'email',
    ]

    list_filter = ['country', 'governorate', 'area', 'type']
    list_per_page = 50
    ordering = ['country', 'governorate', 'area', 'provider']

    fieldsets = (
        ('الموقع / Location', {
            'fields': (
                ('country', 'country_ar'),
                ('governorate', 'governorate_ar'),
                ('area', 'area_ar'),
            )
        }),
        ('التصنيف / Classification', {
            'fields': (
                ('type', 'type_ar'),
                ('speciality', 'speciality_ar'),
            )
        }),
        ('مقدم الخدمة / Provider', {
            'fields': (
                ('provider', 'provider_ar'),
                ('address', 'address_ar'),
            )
        }),
        ('بيانات التواصل / Contact', {
            'fields': ('phone', 'website', 'email', 'notes'),
        }),
    )

    def address_short(self, obj):
        return (obj.address[:40] + '...') if obj.address and len(obj.address) > 40 else obj.address
    address_short.short_description = 'Address'

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
