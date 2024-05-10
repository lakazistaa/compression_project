from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register each model with the admin site
admin.site.register(Utilisateur)
admin.site.register(Modele)
admin.site.register(JeuDeDonnees)
admin.site.register(MethodeCompression)
admin.site.register(Tache)
admin.site.register(ModeleCompresse)
admin.site.register(ResultatEvaluation)
admin.site.register(MetriqueCompression)