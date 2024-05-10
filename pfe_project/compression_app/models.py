from django.db import models

# prendre les corrections de amamra (40%)

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100)

class Modele(models.Model):
    nom = models.CharField(max_length=255)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    parametres_compression = models.TextField()
    path = models.CharField(max_length=255)


class JeuDeDonnees(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    path = models.CharField(max_length=255)


class MethodeCompression(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    taux_compression = models.FloatField()

class Tache(models.Model):
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    resultats = models.TextField()
    jeux_de_donnees = models.ForeignKey(JeuDeDonnees, on_delete=models.CASCADE)
    
class ModeleCompresse(models.Model):
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
    rapport = models.TextField()
    metrics = models.TextField()
    path = models.CharField(max_length=255)

class ResultatEvaluation(models.Model):
    resultat_compression = models.ForeignKey(ModeleCompresse, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    details = models.TextField()

class MetriqueCompression(models.Model):
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
    valeur = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

