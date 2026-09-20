from django.urls import path
from django.contrib import admin
from django.views.i18n import set_language
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ كل الـ app URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # ===== Medical Networks =====
    path('discount/', views.network, name='network'),
    path('eds/', views.eds, name='eds'),
    path('mofa/', views.mofa, name='mofa'),
    path('exxon/', views.exxon, name='exxon'),
    path('emfa/', views.emfa, name='emfa'),
    path('horizon/', views.horizon, name='horizon'),
    path('horizon-global/', views.horizon_global_network, name='horizon_global_network'),

    # ===== PreAuth =====
    path('preauth/', views.preauth_view, name='preauth'),

    # ===== AJAX =====
    path('get-areas/', views.get_areas, name='get_areas'),
    path('get-types/', views.get_types, name='get_types'),
    path('ajax/mofa/areas/', views.get_areas_mofa, name='get_areas_mofa'),
    path('ajax/mofa/types/', views.get_types_mofa, name='get_types_mofa'),
    path('ajax/exxon/areas/', views.get_areas_exxon, name='get_areas_exxon'),
    path('ajax/exxon/types/', views.get_types_exxon, name='get_types_exxon'),
    path('ajax/emfa/filter/', views.emfa_filter_ajax, name='emfa_filter_ajax'),
    path('ajax/emfa/governorates/', views.get_governorates_emfa, name='get_governorates_emfa'),
    path('ajax/emfa/areas/', views.get_areas_emfa, name='get_areas_emfa'),
    path('ajax/emfa/types/', views.get_types_emfa, name='get_types_emfa'),
    path('ajax/emfa/specialities/', views.get_specialities_emfa, name='get_specialities_emfa'),
    path('ajax/horizon/areas/', views.get_areas_horizon, name='get_areas_horizon'),
    path('ajax/horizon/types/', views.get_types_horizon, name='get_types_horizon'),
    path('ajax/horizon-global/areas/', views.get_areas_horizon_global, name='get_areas_horizon_global'),
    path('ajax/horizon-global/types/', views.get_types_horizon_global, name='get_types_horizon_global'),
    path('ajax/eds/areas/', views.get_areas_eds, name='get_areas_eds'),
    path('ajax/eds/types/', views.get_types_eds, name='get_types_eds'),

    # ✅ Language switching — Django's built-in view (handles session key + cookie correctly)
    path('set-language/', set_language, name='set_language'),
]