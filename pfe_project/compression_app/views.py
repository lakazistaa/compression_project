import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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


# ------------------ JeuDeDonnees --------------------------------
def jeux_de_donnees_list_view(request):
    return render(request, 'compression_app/jeux_de_donnees/list.html')


# ----------------- MethodeCompression --------------------------------
def methodes_compression_list_view(request):
    return render(request, 'compression_app/methodes_compression/list.html')

# ----------------- Tache --------------------------------
def taches_list_view(request):
    return render(request, 'compression_app/taches/list.html')

#------------------- compress_model ----------------------------------------------------

def compress_model(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dataset_id = data.get('dataset')
        method_id = data.get('method')
        taux_compression = data.get('taux_compression')
        metric_id= data.get('metric')
        modele_id = data.get('modele')

        dataset = get_object_or_404(JeuDeDonnees, pk=dataset_id)
        method = get_object_or_404(MethodeCompression, pk=method_id)
        metric = get_object_or_404(MetriqueCompression, pk=metric_id)
        modele = get_object_or_404(Modele, pk=modele_id)

        tache = Tache.objects.create(
            jeux_de_donnees=dataset,
            taux_compression=taux_compression,
            metrique_compression=metric,
            methode_compression=method,
            modele=modele,
        )
        tache.save()

        return JsonResponse({'status': 'success'})

    else:
        methods = MethodeCompression.objects.all()
        metrics = MetriqueCompression.objects.all()
        modeles = Modele.objects.all()
        return render(request, 'compression_app/compresser_modele/index.html', { 'methods': methods, 'metrics': metrics, 'modeles': modeles})

def upload_model(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        file_path = handle_uploaded_file(file)
        return JsonResponse({'file_path': file_path})

    return HttpResponse(status=405)

def handle_uploaded_file(file):
    import os
    from django.conf import settings
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path

