from django.shortcuts import render
from .models import Docente, HistoriaVideo, Estudiantes
from packages.models import Tema, Capitulo


# Create your views here.

def home(request):
    docentes = Docente.objects.all()
    videos = HistoriaVideo.objects.exclude(reel__isnull=True).exclude(reel__exact='')
    estudiantes = Estudiantes.objects.all()
    temas = Tema.objects.all()
    capitulos = Capitulo.objects.all()

    return render(request, 'home.html', {
        'docentes': docentes,
        'videos': videos,
        'estudiantes': estudiantes,
        'capitulos': capitulos,
        'temas': temas,
    })


def ponents(request):
    docentes = Docente.objects.all()
    return render(request, 'ponents.html', {
        'docentes': docentes,
    })
