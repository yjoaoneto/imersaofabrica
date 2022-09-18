from django.forms import ModelForm
from .models import Formulario

class FormularioPostagem(ModelForm):

    class Meta:
        model = Formulario
        fields = ['classe', 'email','valor']