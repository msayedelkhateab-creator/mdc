from django.contrib import admin
from .models import Networkar,Networkedsar,Networkexxonar,Networkemfaar,Networkmofaar,Networkhorizonar
from import_export.admin import ImportExportModelAdmin
from django.db import models
# Register your models here.

@admin.register(Networkar)
class NetworkarAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']


@admin.register(Networkedsar)
class NetworkarAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']

@admin.register(Networkmofaar)
class NetworkarAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']

@admin.register(Networkexxonar)
class NetworkarAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']
@admin.register(Networkemfaar)
class NetworkarAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']


@admin.register(Networkhorizonar)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ['governorate','area','type','speciality','provider','address','phone']
    list_display_links = ['provider', 'phone']
    search_fields = ['governorate','area','type','speciality','provider','address','phone']
    list_filter = ['provider','governorate','area']
