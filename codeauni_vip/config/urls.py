"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path
from main.views import home, ponents, business, syllabus_bussines, guardar_formulario, guardar_formulario_free, syllabus, guardar_formulario_profesional, guardar_formulario_bussines, free_formulario_bussines

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ponentes/', ponents, name='ponents'),
    path('business/', business, name='business'),
    path('temario/<int:curso_id>/', syllabus, name='syllabus'),
    path('temario-business/<int:curso_id>/', syllabus_bussines, name='syllabus_bussines'),


    path('api/guardar-formulario/', guardar_formulario, name='guardar_formulario'),
    path('api/guardar-formulario-profesional/', guardar_formulario_profesional, name='guardar_formulario-profesional'),
    path('api/guardar_formulario_free/', guardar_formulario_free, name='guardar_formulario_free'),
    path('api/guardar_formulario_bussines/', guardar_formulario_bussines, name='guardar_formulario_bussines'),
    path('api/free_formulario_bussines/', free_formulario_bussines, name='free_formulario_bussines'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "CODEa VIP"
admin.site.index_title = "Panel de administración | Codea VIP"
