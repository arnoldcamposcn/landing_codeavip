from django.shortcuts import render
from .models import Docente, HistoriaVideo, Estudiantes, DocenteBusiness, EstudiantesBusiness,HistoriaVideoBusiness, MembresiaFormulario
from packages.models import Tema, Capitulo
from packages_business.models import TemaBusiness, CapituloBusiness
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


# Create your views here.

def home(request):
    docentes = Docente.objects.all()
    videos = HistoriaVideo.objects.exclude(reel__isnull=True).exclude(reel__exact='')
    estudiantes = Estudiantes.objects.all()
    temas = Tema.objects.all()

    capitulos_ondemand = Capitulo.objects.filter(tipo_entrega='ondemand')
    capitulos_envivo = Capitulo.objects.filter(tipo_entrega='envivo')

    return render(request, 'home.html', {
        'docentes': docentes,
        'videos': videos,
        'estudiantes': estudiantes,
        'temas': temas,
        'capitulos_ondemand': capitulos_ondemand,
        'capitulos_envivo': capitulos_envivo,
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

    capitulos_ondemand = CapituloBusiness.objects.filter(tipo_entrega='ondemand')
    capitulos_envivo = CapituloBusiness.objects.filter(tipo_entrega='envivo')

    return render(request, 'pages/business.html', {
        'docentes': docentes,
        'videos': videos,
        'estudiantes': estudiantes,
        'temas': temas,
        'capitulos_ondemand': capitulos_ondemand,
        'capitulos_envivo': capitulos_envivo,
    })


@csrf_exempt
def guardar_formulario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            MembresiaFormulario.objects.create(
                nombre=data.get('nombre'),
                apellido=data.get('apellido'),
                telefono=data.get('telefono'),
                correo=data.get('correo'),
                pais=data.get('pais'),
                especializacion=data.get('especializacion'),
                perfil=data.get('perfil'),
                membresia=int(data.get('membresia'))
            )

            return JsonResponse({'ok': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)