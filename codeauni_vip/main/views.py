from django.shortcuts import render
from collections import defaultdict
from django.shortcuts import get_object_or_404
from .models import datos_corporativos, Docente, MembresiaVIP,  Clientes,HistoriaVideoBusiness, membresia_estudiantes, prueba_gratuita_vip, membresia_profesionales, membresia_bussines, membresia_free_bussines, marcas_bussines
from packages.models import Tema, Curso, Temario as TemarioNormal, TipoContenido, TipoModulo
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
import json


def home(request):
    docentes = Docente.objects.all()
    estudiantes = Clientes.objects.all()
    corporativos = datos_corporativos.objects.all()
    temas = Tema.objects.all()
    capitulos_ondemand = Curso.objects.filter(
        tipo_entrega='ondemand',
        mostrar_en_vip=True  
    ).select_related('tipo_contenido', 'tema')

    capitulos_envivo = Curso.objects.filter(
        tipo_entrega='envivo',
        mostrar_en_vip=True  
    ).select_related('tipo_contenido', 'tema')

    membresias = MembresiaVIP.objects.all().order_by('precio')
    historias_videos = HistoriaVideoBusiness.objects.all()

    # Agrupar temarios y módulos por curso
    temarios_por_curso = defaultdict(list)
    modulos_por_curso = defaultdict(set)

    for temario in TemarioNormal.objects.select_related('curso', 'tipo_modulo'):
        temarios_por_curso[temario.curso.id].append(temario)
        modulos_por_curso[temario.curso.id].add(temario.tipo_modulo)

    return render(request, 'home.html', {
        'docentes': docentes,
        'estudiantes': estudiantes,
        'corporativos': corporativos,
        'temas': temas,
        'capitulos_ondemand': capitulos_ondemand,
        'capitulos_envivo': capitulos_envivo,
        'membresias': membresias,
        'historias_videos': historias_videos,
        'temarios_por_curso': dict(temarios_por_curso),
        'modulos_por_curso': {k: list(v) for k, v in modulos_por_curso.items()},
    })


def business(request):
    docentes = Docente.objects.all()
    historias_videos = HistoriaVideoBusiness.objects.all()
    estudiantes = Clientes.objects.all()
    cursos = Tema.objects.all()

    temas = Tema.objects.all()
    marcas = marcas_bussines.objects.all()

    capitulos_ondemand = (
        Curso.objects.filter(
            tipo_entrega='ondemand',
            mostrar_en_business=True 
        ).select_related('tipo_contenido', 'tema')
    )

    capitulos_envivo = (
        Curso.objects.filter(
            tipo_entrega='envivo',
            mostrar_en_business=True  
        ).select_related('tipo_contenido', 'tema')
    )

    temarios_por_curso = defaultdict(list)
    modulos_por_curso = defaultdict(set)

    for temario in TemarioNormal.objects.select_related('curso', 'tipo_modulo'):
        temarios_por_curso[temario.curso.id].append(temario)
        modulos_por_curso[temario.curso.id].add(temario.tipo_modulo)

    return render(request, 'pages/bussines.html', {
        'docentes': docentes,
        'historias_videos': historias_videos,
        'estudiantes': estudiantes,
        'temas': temas,
        'capitulos_ondemand': capitulos_ondemand,
        'capitulos_envivo': capitulos_envivo,
        'cursos': cursos,
        'marcas': marcas,
        'temarios_por_curso': dict(temarios_por_curso),
        'modulos_por_curso': {k: list(v) for k, v in modulos_por_curso.items()},
    })


def ponents(request):
    docentes = Docente.objects.all()
    return render(request, 'ponents.html', {
        'docentes': docentes,
    })



def syllabus(request, curso_id):
    curso = get_object_or_404(
        Curso.objects.select_related('tema'), 
        id=curso_id
    )
    temarios = TemarioNormal.objects.filter(
        curso=curso
    ).select_related('tipo_modulo').order_by('tipo_modulo')

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
    curso = get_object_or_404(
        Curso.objects.select_related('tema'),  # Agregamos select_related para optimizar
        id=curso_id
    )

    temarios = TemarioNormal.objects.filter(
        curso=curso
    ).select_related('tipo_modulo').order_by('tipo_modulo')

    modulos = {}
    for temario in temarios:
        modulo_key = temario.tipo_modulo
        if modulo_key not in modulos:
            modulos[modulo_key] = []
        modulos[modulo_key].append(temario)

    return render(request, 'home.html', {
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
