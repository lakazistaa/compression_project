from django.db import models

# prendre les corrections de amamra (40%)

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100)

class JeuDeDonnees(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    path = models.CharField(max_length=255)

class Modele(models.Model):
    nom = models.CharField(max_length=255)
    jeu_de_donnees = models.ForeignKey(JeuDeDonnees, on_delete=models.CASCADE)
    #utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    description = models.TextField()
    path = models.CharField(max_length=255)

class MethodeCompression(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()

class MetriqueCompression(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()

#metrique evaluation
class MetriqueEvaluation(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    

class ModeleCompresse(models.Model):
    nom= models.CharField(max_length=255)
    path = models.CharField(max_length=255)

class Tache(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    taux_compression = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE)

    finished = models.BooleanField(default=False)
    jeux_de_donnees = models.ForeignKey(JeuDeDonnees, on_delete=models.CASCADE)
    methode_compression = models.ForeignKey(MethodeCompression, on_delete=models.CASCADE)
    metrique_compression = models.ForeignKey(MetriqueCompression, on_delete=models.CASCADE)

    
class ResultatEvaluation(models.Model):
    modele_compresse = models.ForeignKey(ModeleCompresse, on_delete=models.CASCADE)
    metrique_evaluation = models.ForeignKey(MetriqueEvaluation, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)



