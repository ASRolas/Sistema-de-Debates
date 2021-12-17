from django.shortcuts import render, redirect
from app.forms import UsuarioForm, PostagemForm
from app.models import Usuario, Postagem


# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = UsuarioForm
    return render(request, 'login.html', data)

def reg(request):
    data = {}
    data['reg'] = UsuarioForm
    return render(request, 'signup.html', data)

def part(request):
    return render(request, 'usuarios.html')


def create(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    return render(request, 'view.html', data)