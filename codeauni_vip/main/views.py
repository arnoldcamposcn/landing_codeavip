from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Docente, HistoriaVideo, Estudiantes, DocenteBusiness, EstudiantesBusiness,HistoriaVideoBusiness, membresia_estudiantes, prueba_gratuita_vip, membresia_profesionales, membresia_bussines, membresia_free_bussines, marcas_bussines
from packages_business.models import TemaBusiness, CursoBusiness, Temario as TemarioBusiness
from packages.models import Tema, Curso, Temario as TemarioNormal
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
import json

# Create your views here.

def home(request):
    docentes = Docente.objects.all()
    videos = HistoriaVideo.objects.exclude(reel__isnull=True).exclude(reel__exact='')
    estudiantes = Estudiantes.objects.all()
    cursos = Curso.objects.all()
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
        'cursos': cursos,
    })


def business(request):
    docentes = DocenteBusiness.objects.all()
    videos = HistoriaVideoBusiness.objects.exclude(reel__isnull=True).exclude(reel__exact='')
    estudiantes = EstudiantesBusiness.objects.all()
    cursos = CursoBusiness.objects.all()

    temas = TemaBusiness.objects.all()
    marcas = marcas_bussines.objects.all()

    capitulos_ondemand = CursoBusiness.objects.filter(tipo_entrega='ondemand')
    capitulos_envivo = CursoBusiness.objects.filter(tipo_entrega='envivo')

    return render(request, 'pages/bussines.html', {
        'docentes': docentes,
        'videos': videos,
        'estudiantes': estudiantes,
        'temas': temas,
        'capitulos_ondemand': capitulos_ondemand,
        'capitulos_envivo': capitulos_envivo,
        'cursos': cursos,
        'marcas': marcas,
    })




def ponents(request):
    docentes = Docente.objects.all()
    return render(request, 'ponents.html', {
        'docentes': docentes,
    })






def syllabus(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    # Filtrar solo los temarios de ese curso
    temarios = TemarioNormal.objects.filter(curso=curso).order_by('tipo_modulo', 'orden')

    # Agrupar temarios por tipo de módulo
    modulos = {}
    for temario in temarios:
        modulo_key = temario.tipo_modulo
        if modulo_key not in modulos:
            modulos[modulo_key] = []
        modulos[modulo_key].append(temario)

    return render(request, 'syllabus.html', {
        'modulos': modulos,
        'curso': curso,
    })




def syllabus_bussines(request, curso_id):
    curso = get_object_or_404(CursoBusiness, id=curso_id)

    # Filtrar solo los temarios de ese curso
    temarios = TemarioBusiness.objects.filter(curso=curso).order_by('tipo_modulo', 'orden')

    # Agrupar temarios por tipo de módulo
    modulos = {}
    for temario in temarios:
        modulo_key = temario.tipo_modulo
        if modulo_key not in modulos:
            modulos[modulo_key] = []
        modulos[modulo_key].append(temario)

    return render(request, 'pages/syllabus_bussines.html', {
        'modulos': modulos,
        'curso': curso,
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
def guardar_formulario_profesional(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            nuevo_registro = membresia_profesionales.objects.create(
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

            nuevo_registro = prueba_gratuita_vip.objects.create(
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



@csrf_exempt
def guardar_formulario_bussines(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Validar membresía
            try:
                membresia = int(data.get('membresia', 1))
            except (ValueError, TypeError):
                membresia = 1  # fallback por defecto

            nuevo_registro = membresia_bussines.objects.create(
                nombre_empresa=data.get('nombre_empresa'),
                nombre_encargado=data.get('nombre_encargado'),
                sitio_web=data.get('sitio_web'),
                telefono=data.get('telefono'),
                correo=data.get('correo'),
                pais=data.get('pais'),
                membresia=membresia
            )

            # Enviar correo de agradecimiento
            send_mail(
                subject='Gracias por solicitar información',
                message=(
                    f"Hola {nuevo_registro.nombre_encargado},\n\n"
                    f"Gracias por solicitar información sobre nuestras {nuevo_registro.get_membresia_display()} en CODEa VIP. "
                    f"Pronto un asesor se pondrá en contacto contigo.\n\n"
                    f"Saludos,\nEl equipo de CODEa"
                ),
                from_email=None,  # Usa DEFAULT_FROM_EMAIL de settings.py
                recipient_list=[nuevo_registro.correo],
                fail_silently=False
            )

            return JsonResponse({'ok': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)




@csrf_exempt
def free_formulario_bussines(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            nuevo_registro = membresia_free_bussines.objects.create(
                nombre_empresa=data.get('nombre_empresa'),
                nombre_encargado=data.get('nombre_encargado'),
                sitio_web=data.get('sitio_web'),
                telefono=data.get('telefono'),
                correo=data.get('correo'),
                pais=data.get('pais')
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
