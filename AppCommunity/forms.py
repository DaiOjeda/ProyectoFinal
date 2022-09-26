from django import forms

class GrupoFormulario(forms.Form):
    camada = forms.IntegerField()
    nombre_lider = forms.CharField(max_length=30)
    apellido_lider = forms.CharField(max_length=30)