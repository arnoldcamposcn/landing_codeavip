from django.shortcuts import render
from .models import Docente, HistoriaVideo, Estudiantes, DocenteBusiness, EstudiantesBusiness,HistoriaVideoBusiness
from packages.models import Tema, Capitulo, TemaBusiness, CapituloBusiness


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



def business(request):
    docentes = DocenteBusiness.objects.all()
    videos = HistoriaVideoBusiness.objects.exclude(reel__isnull=True).exclude(reel__exact='')
    estudiantes = EstudiantesBusiness.objects.all()
    temas = TemaBusiness.objects.all()
    capitulos = CapituloBusiness.objects.all()

    return render(request, 'pages/business.html', {
        'docentes': docentes,
        'videos': videos,
        'estudiantes': estudiantes,
        'capitulos': capitulos,
        'temas': temas,
    })