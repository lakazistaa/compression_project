from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('dashboard/', dashboard_view, name='dashboard'),

    # ----------------------- utilisateur -----------------------
    path('utilisateurs/', utilisateurs_list_view, name='utilisateurs'),
    path('get_utilisateurs/', get_utilisateurs, name='get_utilisateurs'),
    path('get_utilisateur_byid/<int:utilisateur_id>/', get_utilisateur_byid, name='get_utilisateur_byid'),
    path('update_user/', update_user, name='update_user'),
    path('utilisateurs/add/', add_modify_utilisateur, name='add_utilisateur'),
    path('utilisateurs/edit/<int:utilisateur_id>/', add_modify_utilisateur, name='modify_utilisateur'),
    path('utilisateurs/delete/<int:utilisateur_id>/', delete_utilisateur, name='delete_utilisateur'),

    # ----------------------- dataset -----------------------
    path('jeux-de-donnees/', jeux_de_donnees_list_view, name='jeux_de_donnees'),
    path('get_jeux-de-donnees/', get_jeux_de_donnees, name='get_jeux_de_donnees'),
    path('jeux-de-donnees/add/', add_modify_jeu_de_donnees, name='add_jeu_de_donnees'),
    path('jeux-de-donnees/edit/<int:jeu_id>/', add_modify_jeu_de_donnees, name='modify_jeu_de_donnees'),
    path('jeux-de-donnees/delete/<int:jeu_id>/', delete_jeu_de_donnees, name='delete_jeu_de_donnees'),

    # ----------------------- compression -----------------------
    path('methodes-compression/', methodes_compression_list_view, name='methodes_compression'),
    path('get_methodes-compression/', get_methodes_compression, name='get_methodes_compression'),
    path('methodes-compression/add/', add_modify_methode_compression, name='add_methode_compression'),
    path('methodes-compression/edit/<int:methode_id>/', add_modify_methode_compression, name='modify_methode_compression'),
    path('methodes-compression/delete/<int:methode_id>/', delete_methode_compression, name='delete_methode_compression'),

    
]