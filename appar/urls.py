from django.urls import path
from . import views

urlpatterns = [
    path('', views.homear, name='homear'),  # Assuming home view for Arabic home
    path('aboutar/', views.aboutar, name='aboutar'),
    path('contactar/', views.contactar, name='contactar'),

    path('medical_networkar/', views.networkar, name='networkar'),
    path('medical_networkar/get-areas/', views.get_areas_ar, name='get_areas_ar'),
    path('medical_networkar/get-types/', views.get_types_ar, name='get_types_ar'),

    # EDS (using Networkedsar model)
    path('edsar/', views.edsar, name='edsar'),
    path('edsar/get-areas/', views.get_areas_edsar, name='get_areas_edsar'),
    path('edsar/get-types/', views.get_types_edsar, name='get_types_edsar'),

    # MOFA
    path('mofaar/', views.mofaar, name='mofaar'),
    path('mofaar/get-areas/', views.get_areas_mofaar, name='get_areas_mofaar'),
    path('mofaar/get-types/', views.get_types_mofaar, name='get_types_mofaar'),

    # EXXON
    path('exxonar/', views.exxonar, name='exxonar'),
    path('exxonar/get-areas/', views.get_areas_exxonar, name='get_areas_exxonar'),
    path('exxonar/get-types/', views.get_types_exxonar, name='get_types_exxonar'),

    # EMFA
    path('emfaar/', views.emfaar, name='emfaar'),
    path('emfaar/get-areas/', views.get_areas_emfaar, name='get_areas_emfaar'),
    path('emfaar/get-types/', views.get_types_emfaar, name='get_types_emfaar'),

    # HORIZON
    path('horizonar/', views.horizonar, name='horizonar'),
    path('horizonar/get-areas/', views.get_areas_horizonar, name='get_areas_horizonar'),
    path('horizonar/get-types/', views.get_types_horizonar, name='get_types_horizonar'),
]
