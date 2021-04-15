from django.shortcuts import render,redirect
from .models import Projeto
from contatos.forms import ContatoForm

# Create your views here.
def home(request):
    contexto = {}
    projetos = Projeto.objects.filter(concluido=True)
    


    contexto['projetos'] = projetos
    if request.method != 'POST':
        form = ContatoForm(request.POST)
        contexto['form'] = form
        return render(request, 'base.html',contexto)



    return render(request, 'base.html', contexto)

def contato(request):
    contexto = {}
    form = ContatoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

