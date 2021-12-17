from django.forms import ModelForm
from app.models import Usuario, Postagem

# Create the form class.
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'senha']

class PostagemForm(ModelForm):
    class Meta:
        model = Postagem
        fields = ['titulo', 'data', 'postagem', 'postador']