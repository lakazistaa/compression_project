# forms.py

from django import forms
from .models import Utilisateur, Modele, JeuDeDonnees, MethodeCompression, Tache, ModeleCompresse, ResultatEvaluation, MetriqueCompression

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class ModeleForm(forms.ModelForm):
    class Meta:
        model = Modele
        fields = '__all__'

class JeuDeDonneesForm(forms.ModelForm):
    class Meta:
        model = JeuDeDonnees
        fields = '__all__'

class MethodeCompressionForm(forms.ModelForm):
    class Meta:
        model = MethodeCompression
        fields = '__all__'

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = '__all__'

class ModeleCompresseForm(forms.ModelForm):
    class Meta:
        model = ModeleCompresse
        fields = '__all__'

class ResultatEvaluationForm(forms.ModelForm):
    class Meta:
        model = ResultatEvaluation
        fields = '__all__'

class MetriqueCompressionForm(forms.ModelForm):
    class Meta:
        model = MetriqueCompression
        fields = '__all__'
