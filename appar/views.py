from django.shortcuts import render
from .models import Networkar, Networkmofaar, Networkexxonar, Networkemfaar, Networkhorizonar, Networkedsar
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required
@staff_member_required
def dashboard(request):
    data = {
        'EDS': Networkedsar.objects.count(),
        'MOFA': Networkmofaar.objects.count(),
        'EXXON': Networkexxonar.objects.count(),
        'EMFA': Networkemfaar.objects.count(),
        'HORIZON': Networkhorizonar.objects.count(),
        'Main Network': Networkar.objects.count(),
    }
    return render(request, 'pages/dashboard.html', {'data': data})


def indexar(request):
    return render(request, 'parts/index.html')


def homear(request):
    return render(request, 'pages/homear.html')


def aboutar(request):
    return render(request, 'pages/aboutar.html')


def contactar(request):
    return render(request, 'pages/contactar.html')


def networkar(request):
    networks = Networkar.objects.all()

    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    if governorate:
        networks = networks.filter(governorate=governorate)
    if area:
        networks = networks.filter(area=area)
    if type:
        networks = networks.filter(type=type)
    if speciality:
        networks = networks.filter(speciality=speciality)
    if query:
        networks = networks.filter(
            Q(provider__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(notes__icontains=query)
        )

    governorates = Networkar.objects.values_list('governorate', flat=True).distinct()
    areas = Networkar.objects.values_list('area', flat=True).distinct()
    types = Networkar.objects.values_list('type', flat=True).distinct()
    specialities = Networkar.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/networkar.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })


def get_areas_ar(request):
    governorate = request.GET.get('governorate')
    areas = Networkar.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})


def get_types_ar(request):
    area = request.GET.get('area')
    types = Networkar.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})


# ========== MOFA ==========

def mofaar(request):
    networks = Networkmofaar.objects.all()
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    if governorate:
        networks = networks.filter(governorate=governorate)
    if area:
        networks = networks.filter(area=area)
    if type:
        networks = networks.filter(type=type)
    if speciality:
        networks = networks.filter(speciality=speciality)
    if query:
        networks = networks.filter(
            Q(provider__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(notes__icontains=query)
        )

    governorates = Networkmofaar.objects.values_list('governorate', flat=True).distinct()
    areas = Networkmofaar.objects.values_list('area', flat=True).distinct()
    types = Networkmofaar.objects.values_list('type', flat=True).distinct()
    specialities = Networkmofaar.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/mofaar.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })


def get_areas_mofaar(request):
    governorate = request.GET.get('governorate')
    areas = Networkmofaar.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})


def get_types_mofaar(request):
    area = request.GET.get('area')
    types = Networkmofaar.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})


# ========== EXXON ==========

def exxonar(request):
    networks = Networkexxonar.objects.all()
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    if governorate:
        networks = networks.filter(governorate=governorate)
    if area:
        networks = networks.filter(area=area)
    if type:
        networks = networks.filter(type=type)
    if speciality:
        networks = networks.filter(speciality=speciality)
    if query:
        networks = networks.filter(
            Q(provider__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(notes__icontains=query)
        )

    governorates = Networkexxonar.objects.values_list('governorate', flat=True).distinct()
    areas = Networkexxonar.objects.values_list('area', flat=True).distinct()
    types = Networkexxonar.objects.values_list('type', flat=True).distinct()
    specialities = Networkexxonar.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/exxonar.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })


def get_areas_exxonar(request):
    governorate = request.GET.get('governorate')
    areas = Networkexxonar.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})


def get_types_exxonar(request):
    area = request.GET.get('area')
    types = Networkexxonar.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})


# ========== EMFA ==========

def emfaar(request):
    networks = Networkemfaar.objects.all()
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    if governorate:
        networks = networks.filter(governorate=governorate)
    if area:
        networks = networks.filter(area=area)
    if type:
        networks = networks.filter(type=type)
    if speciality:
        networks = networks.filter(speciality=speciality)
    if query:
        networks = networks.filter(
            Q(provider__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(notes__icontains=query)
        )

    governorates = Networkemfaar.objects.values_list('governorate', flat=True).distinct()
    areas = Networkemfaar.objects.values_list('area', flat=True).distinct()
    types = Networkemfaar.objects.values_list('type', flat=True).distinct()
    specialities = Networkemfaar.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/emfaar.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })


def get_areas_emfaar(request):
    governorate = request.GET.get('governorate')
    areas = Networkemfaar.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})


def get_types_emfaar(request):
    area = request.GET.get('area')
    types = Networkemfaar.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})


# ========== HORIZON ==========

def horizonar(request):
    networks = Networkhorizonar.objects.all()
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    if governorate:
        networks = networks.filter(governorate=governorate)
    if area:
        networks = networks.filter(area=area)
    if type:
        networks = networks.filter(type=type)
    if speciality:
        networks = networks.filter(speciality=speciality)
    if query:
        networks = networks.filter(
            Q(provider__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(notes__icontains=query)
        )

    governorates = Networkhorizonar.objects.values_list('governorate', flat=True).distinct()
    areas = Networkhorizonar.objects.values_list('area', flat=True).distinct()
    types = Networkhorizonar.objects.values_list('type', flat=True).distinct()
    specialities = Networkhorizonar.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/horizonar.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })


def get_areas_horizonar(request):
    governorate = request.GET.get('governorate')
    areas = Networkhorizonar.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})


def get_types_horizonar(request):
    area = request.GET.get('area')
    types = Networkhorizonar.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})



# Main edsar page with filtering
def edsar(request):
    governorates = Networkedsar.objects.values_list('governorate', flat=True).distinct()
    areas = Networkedsar.objects.values_list('area', flat=True).distinct()
    types = Networkedsar.objects.values_list('type', flat=True).distinct()

    area_filter = request.GET.get('area')
    type_filter = request.GET.get('type')

    queryset = Networkedsar.objects.all()
    if area_filter:
        queryset = queryset.filter(area=area_filter)
    if type_filter:
        queryset = queryset.filter(type=type_filter)

    context = {
        'networks': queryset,
        'governorates': governorates,
        'areas': areas,
        'types': types,
        'selected_area': area_filter,
        'selected_type': type_filter,
    }
    return render(request, 'pages/edsar.html', context)

# AJAX: get areas for edsar
def get_areas_edsar(request):
    areas = Networkedsar.objects.values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})

# AJAX: get types for edsar
def get_types_edsar(request):
    types = Networkedsar.objects.values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})
