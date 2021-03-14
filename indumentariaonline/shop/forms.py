from django.forms import ModelForm
from .models import Remera

class FormularioRemera(ModelForm):
    class Meta:
        model = Remera
        fields = ("marca", "talle", "color", "lisa", "genero")





 

