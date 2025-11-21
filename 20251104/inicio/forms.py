import django.forms as forms
class CrearAuto (forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    imagen = forms.ImageField(required=False)
class BuscarAuto(forms.Form):
    modelo = forms.CharField(max_length=30, required=False)