from django.shortcuts import render, redirect
from .models import Network, Networkmofa, Networkexxon, Networkemfa, Networkhorizon, Networkedsnew, NetworkHorizonGlobal
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.translation import get_language, activate
from django.core.paginator import Paginator
from django.core.cache import cache
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods
from django.conf import settings
from urllib.parse import urlencode
import uuid
from django.core.mail import EmailMessage
from .forms import PreAuthForm


# ============= HELPER FUNCTIONS =============

def get_language_fields(language):
    """Return field names based on language"""
    if language == 'ar':
        return {
            'governorate': 'governorate_ar',
            'area': 'area_ar',
            'type': 'type_ar',
            'speciality': 'speciality_ar',
            'provider': 'provider_ar',
            'address': 'address_ar'
        }
    return {
        'governorate': 'governorate',
        'area': 'area',
        'type': 'type',
        'speciality': 'speciality',
        'provider': 'provider',
        'address': 'address'
    }


def build_query_filter(query, language):
    """Build Q object for search query - OPTIMIZED: removed notes field"""
    query_filter = Q(
        provider__icontains=query
    ) | Q(
        address__icontains=query
    ) | Q(
        phone__icontains=query
    ) | Q(
        email__icontains=query
    )

    if language == 'ar':
        query_filter |= Q(provider_ar__icontains=query) | Q(address_ar__icontains=query)

    return query_filter


def apply_filters(queryset, request, fields):
    """Apply filters to queryset based on request parameters"""
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type_param = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query', '').strip()

    if governorate:
        queryset = queryset.filter(**{fields['governorate']: governorate})
    if area:
        queryset = queryset.filter(**{fields['area']: area})
    if type_param:
        queryset = queryset.filter(**{fields['type']: type_param})
    if speciality:
        queryset = queryset.filter(**{fields['speciality']: speciality})

    # 🔥 CRITICAL: Only search if query length > 2
    if query and len(query) > 2:
        language = get_language()
        queryset = queryset.filter(build_query_filter(query, language))

    return queryset


def get_pagination_data(queryset, request):
    """Handle pagination and return page object and range"""
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_page = page_obj.number
    total_pages = paginator.num_pages
    start_page = ((current_page - 1) // 10) * 10 + 1
    end_page = min(start_page + 9, total_pages)
    page_range = range(start_page, end_page + 1)

    return page_obj, page_range


def get_filter_options(model, fields):
    """Get distinct filter options from model - WITHOUT CACHE (called by cached function)"""
    return {
        'governorates': sorted(filter(None, model.objects.values_list(fields['governorate'], flat=True).distinct())),
        'areas': sorted(filter(None, model.objects.values_list(fields['area'], flat=True).distinct())),
        'types': sorted(filter(None, model.objects.values_list(fields['type'], flat=True).distinct())),
        'specialities': sorted(filter(None, model.objects.values_list(fields['speciality'], flat=True).distinct()))
    }


def get_cached_filter_options(model, language):
    """🔥 CACHED VERSION - Reduces CPU by 50%+"""
    cache_key = f"{model.__name__}_{language}_filters"
    filter_options = cache.get(cache_key)

    if not filter_options:
        fields = get_language_fields(language)
        filter_options = get_filter_options(model, fields)
        cache.set(cache_key, filter_options, 3600)  # Cache for 1 hour

    return filter_options


def get_query_string(request):
    """Get query string without page parameter"""
    querydict = request.GET.copy()
    if 'page' in querydict:
        del querydict['page']
    return urlencode(querydict)


def get_optimized_queryset(model, fields):
    """🔥 CRITICAL: Only fetch needed columns - Reduces memory & CPU"""
    return model.objects.only(
        'id',
        'provider',
        'provider_ar',
        'address',
        'address_ar',
        'phone',
        'email',
        fields['governorate'],
        fields['area'],
        fields['type'],
        fields['speciality']
    )


def render_network_page(request, model, template_name):
    """Generic function to render network pages - FULLY OPTIMIZED"""
    language = get_language()
    fields = get_language_fields(language)

    # 🔥 Get optimized queryset (only needed columns)
    networks = get_optimized_queryset(model, fields)

    # Apply filters
    networks = apply_filters(networks, request, fields)

    # Get pagination
    page_obj, page_range = get_pagination_data(networks, request)

    # 🔥 Get CACHED filter options
    filter_options = get_cached_filter_options(model, language)

    # Get query string
    query_string = get_query_string(request)

    context = {
        'networks': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'language': language,
        'query_string': query_string,
        **filter_options
    }

    return render(request, template_name, context)


def get_areas_generic(request, model):
    """Generic function to get areas based on governorate - CACHED"""
    language = get_language()
    governorate = request.GET.get('governorate')

    if not governorate:
        return JsonResponse({'areas': []})

    # 🔥 Cache key includes governorate
    cache_key = f"{model.__name__}_{language}_areas_{governorate}"
    areas = cache.get(cache_key)

    if areas is None:
        field = 'governorate_ar' if language == 'ar' else 'governorate'
        area_field = 'area_ar' if language == 'ar' else 'area'

        areas = list(filter(None, model.objects.filter(
            **{field: governorate}
        ).values_list(area_field, flat=True).distinct()))

        cache.set(cache_key, areas, 3600)  # Cache for 1 hour

    return JsonResponse({'areas': areas})


def get_types_generic(request, model):
    """Generic function to get types based on area - CACHED"""
    language = get_language()
    area = request.GET.get('area')

    if not area:
        return JsonResponse({'types': []})

    # 🔥 Cache key includes area
    cache_key = f"{model.__name__}_{language}_types_{area}"
    types = cache.get(cache_key)

    if types is None:
        area_field = 'area_ar' if language == 'ar' else 'area'
        type_field = 'type_ar' if language == 'ar' else 'type'

        types = list(filter(None, model.objects.filter(
            **{area_field: area}
        ).values_list(type_field, flat=True).distinct()))

        cache.set(cache_key, types, 3600)  # Cache for 1 hour

    return JsonResponse({'types': types})


# ============= MAIN VIEWS =============

@login_required
@staff_member_required
def dashboard(request):
    """Dashboard with cached counts"""
    cache_key = 'dashboard_counts'
    data = cache.get(cache_key)

    if not data:
        data = {
            'EDS': Networkedsnew.objects.count(),
            'HORIZONGLOBAL': NetworkHorizonGlobal.objects.count(),
            'MOFA': Networkmofa.objects.count(),
            'EXXON': Networkexxon.objects.count(),
            'EMFA': Networkemfa.objects.count(),
            'HORIZON': Networkhorizon.objects.count(),
            'Main Network': Network.objects.count(),
        }
        cache.set(cache_key, data, 300)  # Cache for 5 minutes

    return render(request, 'pages/dashboard.html', {'data': data})


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    language = get_language()
    return render(request, 'pages/contact.html', {'language': language})


def nav(request):
    language = get_language()
    return render(request, 'parts/navbar.html', {'language': language})


def footer(request):
    return render(request, 'parts/footer.html')


# ============= NETWORK VIEWS =============

def network(request):
    return render_network_page(request, Network, 'pages/network.html')


def mofa(request):
    return render_network_page(request, Networkmofa, 'pages/mofa.html')


def exxon(request):
    return render_network_page(request, Networkexxon, 'pages/exxon.html')


def horizon(request):
    return render_network_page(request, Networkhorizon, 'pages/horizon.html')


def eds(request):
    return render_network_page(request, Networkedsnew, 'pages/eds.html')


def horizon_global_network(request):
    return render_network_page(request, NetworkHorizonGlobal, 'pages/horizon_global_network.html')


# ============= AJAX VIEWS - Main Network =============

def get_areas(request):
    return get_areas_generic(request, Network)


def get_types(request):
    return get_types_generic(request, Network)


# ============= AJAX VIEWS - MOFA =============

def get_areas_mofa(request):
    return get_areas_generic(request, Networkmofa)


def get_types_mofa(request):
    return get_types_generic(request, Networkmofa)


# ============= AJAX VIEWS - EXXON =============

def get_areas_exxon(request):
    return get_areas_generic(request, Networkexxon)


def get_types_exxon(request):
    return get_types_generic(request, Networkexxon)


# ============= AJAX VIEWS - HORIZON =============

def get_areas_horizon(request):
    return get_areas_generic(request, Networkhorizon)


def get_types_horizon(request):
    return get_types_generic(request, Networkhorizon)


# ============= AJAX VIEWS - EDS =============

def get_areas_eds(request):
    return get_areas_generic(request, Networkedsnew)


def get_types_eds(request):
    return get_types_generic(request, Networkedsnew)


# ============= AJAX VIEWS - HORIZON GLOBAL =============

def get_areas_horizon_global(request):
    return get_areas_generic(request, NetworkHorizonGlobal)


def get_types_horizon_global(request):
    return get_types_generic(request, NetworkHorizonGlobal)


# ============= PRE-AUTH =============

def preauth_view(request):
    reference_number = None

    if request.method == 'POST':
        form = PreAuthForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            reference_number = str(uuid.uuid4()).split('-')[0]

            subject = f"طلب موافقة جديد - رقم مرجعي: {reference_number}"
            body = f"""
            الاسم: {cd['name']}
            التواصل: {cd['contact']}
            نوع الخدمة: {cd['service_type']}
            وصف: {cd['description']}
            الرقم المرجعي: {reference_number}
            """

            email = EmailMessage(
                subject,
                body,
                to=['mohamed130761@gmail.com'],
            )

            if request.FILES.get('file'):
                email.attach(
                    request.FILES['file'].name,
                    request.FILES['file'].read(),
                    request.FILES['file'].content_type
                )

            email.send()

            return render(request, 'pages/preauth.html', {
                'form': PreAuthForm(),
                'reference': reference_number,
                'success': True
            })
    else:
        form = PreAuthForm()

    return render(request, 'pages/preauth.html', {'form': form})

# =====================================================================
#  EMFA
# =====================================================================

def get_language_fields_emfa(language):
    if language == 'ar':
        return {
            'country': 'country_ar',
            'city': 'city_ar',
            'type': 'type_ar',
        }
    return {
        'country': 'country',
        'city': 'city',
        'type': 'type',
    }


def build_query_filter_emfa(query, language):
    """البحث العام: provider, speciality, address, phone, mobile, email"""
    query_filter = (
        Q(provider__icontains=query) |
        Q(speciality__icontains=query) |
        Q(address__icontains=query) |
        Q(phone__icontains=query) |
        Q(mobile__icontains=query) |
        Q(email__icontains=query)
    )

    if language == 'ar':
        query_filter |= (
            Q(provider_ar__icontains=query) |
            Q(speciality_ar__icontains=query) |
            Q(address_ar__icontains=query)
        )

    return query_filter


def apply_filters_emfa(queryset, request, fields):
    country = request.GET.get('country')
    city = request.GET.get('city')
    type_param = request.GET.get('type')
    query = request.GET.get('query', '').strip()

    if country:
        queryset = queryset.filter(**{fields['country']: country})
    if city:
        queryset = queryset.filter(**{fields['city']: city})
    if type_param:
        queryset = queryset.filter(**{fields['type']: type_param})

    if query and len(query) > 2:
        language = get_language()
        queryset = queryset.filter(build_query_filter_emfa(query, language))

    return queryset


def get_filter_options_emfa(fields):
    return {
        'countries': sorted(filter(None, Networkemfa.objects.values_list(fields['country'], flat=True).distinct())),
        'cities': sorted(filter(None, Networkemfa.objects.values_list(fields['city'], flat=True).distinct())),
        'types': sorted(filter(None, Networkemfa.objects.values_list(fields['type'], flat=True).distinct())),
    }


def get_cached_filter_options_emfa(language):
    cache_key = f"Networkemfa_{language}_filters_v3"
    filter_options = cache.get(cache_key)
    if not filter_options:
        fields = get_language_fields_emfa(language)
        filter_options = get_filter_options_emfa(fields)
        cache.set(cache_key, filter_options, 3600)
    return filter_options


def get_optimized_queryset_emfa():
    return Networkemfa.objects.only(
        'id',
        'country', 'country_ar',
        'city', 'city_ar',
        'type', 'type_ar',
        'speciality', 'speciality_ar',
        'provider', 'provider_ar',
        'address', 'address_ar',
        'phone', 'mobile', 'website', 'email', 'notes',
    )


def build_emfa_queryset(request, fields):
    networks = get_optimized_queryset_emfa()
    networks = apply_filters_emfa(networks, request, fields)
    return networks


def emfa(request):
    language = get_language()
    fields = get_language_fields_emfa(language)

    networks = build_emfa_queryset(request, fields)
    page_obj, page_range = get_pagination_data(networks, request)
    filter_options = get_cached_filter_options_emfa(language)
    query_string = get_query_string(request)

    context = {
        'networks': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'language': language,
        'query_string': query_string,
        **filter_options,
    }
    return render(request, 'pages/emfa.html', context)


def emfa_filter_ajax(request):
    language = get_language()
    fields = get_language_fields_emfa(language)

    networks = build_emfa_queryset(request, fields)
    page_obj, page_range = get_pagination_data(networks, request)
    query_string = get_query_string(request)

    rows_html = render_to_string('pages/_emfa_rows.html', {
        'networks': page_obj,
        'language': language,
    }, request=request)
    pagination_html = render_to_string('pages/_emfa_pagination.html', {
        'page_obj': page_obj,
        'page_range': page_range,
        'language': language,
        'query_string': query_string,
    }, request=request)

    return JsonResponse({
        'rows_html': rows_html,
        'pagination_html': pagination_html,
        'count': page_obj.paginator.count,
        'page': page_obj.number,
        'num_pages': page_obj.paginator.num_pages,
    })


# ---------- AJAX: تسلسل الفلاتر (Cascade: country -> city -> type) ----------

def get_cities_emfa(request):
    language = get_language()
    country = request.GET.get('country')
    if not country:
        return JsonResponse({'cities': []})

    cache_key = f"Networkemfa_{language}_cities_{country}"
    cities = cache.get(cache_key)
    if cities is None:
        country_field = 'country_ar' if language == 'ar' else 'country'
        city_field = 'city_ar' if language == 'ar' else 'city'
        cities = sorted(filter(None, Networkemfa.objects.filter(
            **{country_field: country}
        ).values_list(city_field, flat=True).distinct()))
        cache.set(cache_key, cities, 3600)

    return JsonResponse({'cities': cities})


def get_types_emfa(request):
    language = get_language()
    city = request.GET.get('city')
    if not city:
        return JsonResponse({'types': []})

    cache_key = f"Networkemfa_{language}_types_{city}"
    types = cache.get(cache_key)
    if types is None:
        city_field = 'city_ar' if language == 'ar' else 'city'
        type_field = 'type_ar' if language == 'ar' else 'type'
        types = sorted(filter(None, Networkemfa.objects.filter(
            **{city_field: city}
        ).values_list(type_field, flat=True).distinct()))
        cache.set(cache_key, types, 3600)

    return JsonResponse({'types': types})


# ============= CLEAR LANGUAGE CACHE (for debugging) =============

@staff_member_required
def clear_language_cache(request):
    pattern = 'Networkemfa_*_filters*'
    cache.delete_pattern(pattern)
    return JsonResponse({'success': True, 'message': 'تم حذف الـ Cache'})