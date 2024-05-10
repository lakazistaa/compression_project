from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.
def dashboard_view(request):
    return render(request, 'compression_app/dashboard.html')

# ------------------ utilisateur --------------------------------
def utilisateurs_list_view(request):
    return render(request, 'compression_app/utilisateurs/list.html')

def get_utilisateurs(request):
    utilisateurs = list(Utilisateur.objects.values())
    return JsonResponse(utilisateurs, safe=False)

def add_modify_utilisateur(request, utilisateur_id=None):
    if utilisateur_id:
        utilisateur = get_object_or_404(Utilisateur, pk=utilisateur_id)
    else:
        utilisateur = None

    if request.method == 'POST':
        form = UtilisateurForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            action = request.POST.get('action')
            if action == 'save_and_add_another':
                return redirect('add_utilisateur')
            else:
                return redirect('get_utilisateurs')
    else:
        form = UtilisateurForm(instance=utilisateur)

    return render(request, 'compression_app/form.html', {'form': form, 'model_name': 'Utilisateur', 'list_view_name': 'get_utilisateurs'})

def delete_utilisateur(request, utilisateur_id):
    if request.method == 'POST':
        utilisateur = get_object_or_404(Utilisateur, pk=utilisateur_id)
        utilisateur.delete()
        return JsonResponse({'message': 'Utilisateur deleted successfully'}, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)



# ------------------ JeuDeDonnees --------------------------------
def jeux_de_donnees_list_view(request):
    return render(request, 'compression_app/jeux_de_donnees/list.html')

def get_jeux_de_donnees(request):
    jeux_de_donnees = list(JeuDeDonnees.objects.values())
    return JsonResponse(jeux_de_donnees, safe=False)

def add_modify_jeu_de_donnees(request, jeu_de_donnees_id=None):
    if jeu_de_donnees_id:
        jeu_de_donnees = get_object_or_404(JeuDeDonnees, pk=jeu_de_donnees_id)
    else:
        jeu_de_donnees = None

    if request.method == 'POST':
        form = JeuDeDonneesForm(request.POST, instance=jeu_de_donnees)
        if form.is_valid():
            form.save()
            action = request.POST.get('action')
            if action == 'save_and_add_another':
                return redirect('add_jeu_de_donnees')
            else:
                return redirect('get_jeux_de_donnees')
    else:
        form = JeuDeDonneesForm(instance=jeu_de_donnees)

    return render(request, 'compression_app/form.html', {'form': form, 'model_name': 'JeuDeDonnees', 'list_view_name': 'get_jeux_de_donnees'})

def delete_jeu_de_donnees(request, jeu_de_donnees_id):
    if request.method == 'POST':
        jeu_de_donnees = get_object_or_404(JeuDeDonnees, pk=jeu_de_donnees_id)
        jeu_de_donnees.delete()
        return JsonResponse({'message': 'JeuDeDonnees deleted successfully'}, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


# --------------------MethodeCompression --------------------------------
def methodes_compression_list_view(request):
    return render(request, 'compression_app/methodes_compression/list.html')

def get_methodes_compression(request):
    methodes_compression = list(MethodeCompression.objects.values())
    return JsonResponse(methodes_compression, safe=False)

def add_modify_methode_compression(request, methode_compression_id=None):
    if methode_compression_id:
        methode_compression = get_object_or_404(MethodeCompression, pk=methode_compression_id)
    else:
        methode_compression = None

    if request.method == 'POST':
        form = MethodeCompressionForm(request.POST, instance=methode_compression)
        if form.is_valid():
            form.save()
            action = request.POST.get('action')
            if action == 'save_and_add_another':
                return redirect('add_methode_compression')
            else:
                return redirect('get_methodes_compression')
    else:
        form = MethodeCompressionForm(instance=methode_compression)

    return render(request, 'compression_app/form.html', {'form': form, 'model_name': 'MethodeCompression', 'list_view_name': 'get_methodes_compression'})

def delete_methode_compression(request, methode_compression_id):
    if request.method == 'POST':
        methode_compression = get_object_or_404(MethodeCompression, pk=methode_compression_id)
        methode_compression.delete()
        return JsonResponse({'message': 'MethodeCompression deleted successfully'}, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

