from django.shortcuts import render
from ..contatos.models import Contato
from ..turmas.models import Turmas
from ..imagens.models import Imagem
from ..cursos_livres.models import CursosLivres

from ..contatos.forms import ContatoCurso
from ..contatos.forms import EditarContato
from .models import Utilidades


def home(request):
    turmas = Turmas.objects.all()
    cursos_livres = CursosLivres.objects.all()
    mes = Utilidades.objects.filter(atributo='mes').values('valor')[0]['valor']
    return render(request, 'home.html', {'titulo': 'Home', 'turmas': turmas, 'cursos_livres': cursos_livres, 'mes':mes})

def contato(request):
    context = {}
    if request.method == 'POST':
        if 'enviar' in request.POST:
            formContato = ContatoCurso(request.POST)
            if formContato.is_valid():
                contato = Contato(nome=formContato.cleaned_data["nome"], email=formContato.cleaned_data["email"], assunto=formContato.cleaned_data["assunto"], mensagem=formContato.cleaned_data["mensagem"])
                contato.save()
                context['valido'] = True
                formContato = ContatoCurso()
            formAlteracao = EditarContato()
        if 'recuperar' in request.POST:
            formAlteracao = EditarContato(request.POST)
            if formAlteracao.is_valid():
                lista = Contato.objects.filter(email=formAlteracao.cleaned_data["emailAlteracao"])
                if lista:
                    last = lista[lista.count() - 1]
                    formAlteracao = EditarContato()
                    formContato = ContatoCurso(initial={'nome': last.nome, 'email':last.email, 'assunto':last.assunto, 'mensagem':last.mensagem, 'alteracao':last.id})
                    context['flag'] = 'encontrado'
                else:
                    formContato = ContatoCurso()
                    context['flag'] = 'naoEncontrado'
            else:
                formContato = ContatoCurso()
        if 'deletar' in request.POST:
            formContato = ContatoCurso(request.POST)
            if formContato.is_valid():
                id = formContato.cleaned_data["alteracao"]
                instance = Contato.objects.filter(id=id).delete()
            formContato = ContatoCurso()
            formAlteracao = EditarContato()
            context['flag'] = 'deletado'
        if 'editar' in request.POST:
            formContato = ContatoCurso(request.POST)
            if formContato.is_valid():
                id = formContato.cleaned_data["alteracao"]
                instance = Contato.objects.get(id=id)
                instance.nome = formContato.cleaned_data["nome"]
                instance.email = formContato.cleaned_data["email"]
                instance.assunto = formContato.cleaned_data["assunto"]
                instance.mensagem = formContato.cleaned_data["mensagem"]
                instance.save()
                context['valido'] = True
                formContato = ContatoCurso()
            else:
                context['flag'] = 'encontrado'

            formAlteracao = EditarContato()


    else:
        formContato = ContatoCurso()
        formAlteracao = EditarContato()
    context['titulo'] = 'Contato'
    context['formContato'] = formContato
    context['formAlteracao'] = formAlteracao
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
