from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('utilisateurs/', utilisateurs_list_view, name='utilisateurs'),
    path('jeux_de_donnees/', jeux_de_donnees_list_view, name='jeux_de_donnees'),
    path('methodes_compression/', methodes_compression_list_view, name='methodes_compression'),
    #taches
    path('taches/', taches_list_view, name='taches'),
    #----------------------- compress_model ------------------------------
    path('compress_model/', compress_model, name="compress_model"),
    path('upload-model/', upload_model, name='upload_model'),

    
]