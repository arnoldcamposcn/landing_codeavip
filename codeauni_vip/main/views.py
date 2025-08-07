from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Docente, HistoriaVideo, Estudiantes, DocenteBusiness, EstudiantesBusiness,HistoriaVideoBusiness, membresia_estudiantes, prueba_gratuita_estudiantes
from packages_business.models import TemaBusiness, CursoBusiness,CursoBusiness  
from packages.models import Tema, Curso, Temario
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
import json

# Create your views here.

def home(request):
    docentes = Docente.objects.all()
    videos = HistoriaVideo.objects.exclude(reel__isnull=True).exclude(reel__exact='')
    estudiantes = Estudiantes.objects.all()
    temas = Tema.objects.all()

    capitulos_ondemand = Curso.objects.filter(tipo_entrega='ondemand')
    capitulos_envivo = Curso.objects.filter(tipo_entrega='envivo')

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



def syllabus(request):
    # Obtener todos los temarios ordenados por módulo y orden
    curso = Curso.objects.all()

    
    temarios = Temario.objects.all().order_by('tipo_modulo', 'orden')
    
    # Agrupar temarios por módulo
    modulos = {}
    for temario in temarios:
        modulo_key = temario.tipo_modulo
        if modulo_key not in modulos:
            modulos[modulo_key] = []
        modulos[modulo_key].append(temario)
    
    return render(request, 'syllabus.html', {
        'modulos': modulos,
        'curso': curso
    })


def business(request):
    docentes = DocenteBusiness.objects.all()
    videos = HistoriaVideoBusiness.objects.exclude(reel__isnull=True).exclude(reel__exact='')
    estudiantes = EstudiantesBusiness.objects.all()

    temas = TemaBusiness.objects.all()

    capitulos_ondemand = CursoBusiness.objects.filter(tipo_entrega='ondemand')
    capitulos_envivo = CursoBusiness.objects.filter(tipo_entrega='envivo')

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

            nuevo_registro = membresia_estudiantes.objects.create(
                nombre=data.get('nombre'),
                apellido=data.get('apellido'),
                telefono=data.get('telefono'),
                correo=data.get('correo'),
                pais=data.get('pais'),
                especializacion=data.get('especializacion'),
                membresia=int(data.get('membresia'))

            )

            # Enviar correo de agradecimiento
            send_mail(
                subject='Gracias por solicitar información',
                message=f"Hola {nuevo_registro.nombre},\n\nGracias por solicitar información sobre nuestras membresías CODEa VIP. Pronto un asesor se pondrá en contacto contigo.\n\nSaludos,\nEl equipo de CODEa",
                from_email=None,  # usa DEFAULT_FROM_EMAIL
                recipient_list=[nuevo_registro.correo],
                fail_silently=False
            )

            return JsonResponse({'ok': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)




@csrf_exempt
def guardar_formulario_free(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            nuevo_registro = prueba_gratuita_estudiantes.objects.create(
                nombre=data.get('nombre'),
                apellido=data.get('apellido'),
                telefono=data.get('telefono'),
                correo=data.get('correo'),
                pais=data.get('pais'),
                especializacion=data.get('especializacion'),

            )

            send_mail(
                subject='Gracias por solicitar información',
                message=f"Hola {nuevo_registro.nombre},\n\nGracias por solicitar información sobre nuestras membresías CODEa VIP. Pronto un asesor se pondrá en contacto contigo.\n\nSaludos,\nEl equipo de CODEa",
                from_email=None,  # usa DEFAULT_FROM_EMAIL
                recipient_list=[nuevo_registro.correo],
                fail_silently=False
            )

            return JsonResponse({'ok': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)