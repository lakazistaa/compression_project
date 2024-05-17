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

class CompressionForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['jeux_de_donnees', 'metrique_compression']
        widgets = {
            'jeux_de_donnees': forms.Select(attrs={'class': 'form-control'}),
            'taux_compression': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'metrique_compression': forms.Select(attrs={'class': 'form-control'}),
            'methode_compression': forms.Select(attrs={'class': 'form-control'}),
        }

    METRIQUE_CHOICES = [
        ('ssim', 'SSIM'),
        ('l0', 'L0'),
        ('l1', 'L1'),
        ('l2', 'L2'),
    ]

    metrique_compression = forms.ChoiceField(choices=METRIQUE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))