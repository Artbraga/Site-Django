from django.shortcuts import render
from ..contatos.models import Contato
from ..turmas.models import Turmas
from ..imagens.models import Imagem

from Trabalho.contatos.forms import ContatoCurso


def home(request):
    turmas = Turmas.objects.all()
    return render(request, 'home.html', {'titulo': 'Home', 'turmas': turmas})

def contato(request):
    context = {}
    if request.method == 'POST':
        form = ContatoCurso(request.POST)
        print(form.errors)
        if form.is_valid():
            print("oi")
            contato = Contato(nome=form.cleaned_data["name"], email=form.cleaned_data["email"], assunto=form.cleaned_data["assunto"], mensagem=form.cleaned_data["mensagem"])
            contato.save()
            context['valido'] = True
            form = ContatoCurso()
    else:
        form = ContatoCurso()
    context['titulo'] = 'Contato'
    context['form'] = form
    return render(request, 'contato.html', context)

def enfermagem(request):
    return render(request, 'enfermagem.html', {'titulo': 'Enfermagem'})

def instrumentacao(request):
    return render(request, 'instrumentacao.html', {'titulo': 'Instrumentação'})

def livres(request):
    return render(request, 'livres.html', {'titulo': 'Cursos Livres'})

def fotos(request):
    context = {}
    context['instalacoes'] = Imagem.objects.filter(referencia='instalacoes')
    context['enfermagem'] = Imagem.objects.filter(referencia='enfermagem')
    context['instrumentacao'] = Imagem.objects.filter(referencia='instrumentacao')
    context['titulo'] = 'Galeria de Fotos'
    print(context['instalacoes'])
    return render(request, 'fotos.html', context)

def mapa(request):
    return render(request, 'mapa.html', {'titulo': 'Mapa'})
