from ast import For
from ctypes.wintypes import PINT
from fileinput import filename
from ssl import Options
from tarfile import NUL
from urllib import response
from urllib.request import Request
from wsgiref.handlers import read_environ
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from .models import Estudiante, Formacion, Certificado, Tiposdocumentos, Municipios, Tiposformaciones
from django.contrib import messages
from datetime import datetime, timedelta
import random
import string


import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

import pdfkit

from fpdf import FPDF, HTMLMixin


def docpdf(request, id_certificado):
    id_cer = id_certificado
    options = {
                'page-size': 'Letter',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",                
                }
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfd = pdfkit.from_url('http://localhost:8000/pdf/'+str(id_cer), False, options=options, configuration=config)
    response = HttpResponse(pdfd, content_type='application/pdf')
    response ; filename="documento.pdf"
    return response

def pdfv(request, id_certificado):
    certificado_consulta = Certificado.objects.get(id_certificado=id_certificado)
    estudiante_consulta = Estudiante.objects.get(id=certificado_consulta.id_estudiante_id)
    formacion_consulta = Formacion.objects.get(id=certificado_consulta.id_formacion_id)
    context = {'certificado':certificado_consulta, 'estudiante': estudiante_consulta, 'formacion':formacion_consulta}
    return render(request, 'pdf2.html', context)




def pdf_ver(request, id_certificado):
    try:                
        certificado_consulta = Certificado.objects.get(id_certificado=id_certificado)
        estudiante_consulta = Estudiante.objects.get(id=certificado_consulta.id_estudiante_id)
        formacion_consulta = Formacion.objects.get(id=certificado_consulta.id_formacion_id)
        template = get_template('pdf_base.html')
        context = {'certificado':certificado_consulta, 'estudiante': estudiante_consulta, 'formacion':formacion_consulta}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Certificado_formacion.pdf"'
        
        pisa_status = pisa.CreatePDF(html, dest=response)
        return response        
    except:
        pass
    return HttpResponseRedirect(reverse_lazy(certificados))
    
  


# Create your views here.

## Estudiantes

def municipios(request):
    municipioslistados = Municipios.objects.all()
    return render(request, "municipios.html", {'municipios':municipioslistados})   


def home(request):
    estudianteslistados = Estudiante.objects.all()
    tipos_documentoslistados = Tiposdocumentos.objects.all()
    municipios = Municipios.objects.all()
    messages.success(request, '¡Estudiantes listados!')
    return render(request, "gestionEstudiante.html", {"estudiantes": estudianteslistados, "tipos_documentos":tipos_documentoslistados, "municipios":municipios})

def registrarEstudiante(request):
    id_estudiante = request.POST['id_estudiante']
    tipo_doc = request.POST['tipo_doc']
    nombre_1 = request.POST['nombre_1']
    nombre_2 = request.POST['nombre_2']
    apellido_1 = request.POST['apellido_1']
    apellido_2 = request.POST['apellido_2']
    municipio = request.POST['municipio']
    celular = request.POST['celular']
    f_nacimiento = request.POST['f_nacimiento']

    estudiante = Estudiante.objects.create(id_estudiante=id_estudiante, tipo_doc_id=tipo_doc, nombre_1=nombre_1, nombre_2=nombre_2,
                                           apellido_1=apellido_1, apellido_2=apellido_2, municipio_id=municipio, celular=celular, f_nacimiento=f_nacimiento)
    messages.success(request, '¡Estudiante registrado correctamente!')
    return redirect('/')

def edicionEstudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    tipos_documentoslistados = Tiposdocumentos.objects.all()
    municipios = Municipios.objects.all()
    return render(request, "edicionEstudiante.html", {"estudiante": estudiante, "tipos_documentos":tipos_documentoslistados, "municipios":municipios})

def editarEstudiante(request):
    id = request.POST['id']
    id_estudiante = request.POST['id_estudiante']
    tipo_doc = request.POST['tipo_doc']
    nombre_1 = request.POST['nombre_1']
    nombre_2 = request.POST['nombre_2']
    apellido_1 = request.POST['apellido_1']
    apellido_2 = request.POST['apellido_2']
    municipio = request.POST['municipio']
    celular = request.POST['celular']
    f_nacimiento = request.POST['f_nacimiento']

    estudiante = Estudiante.objects.get(id=id)
    estudiante.id_estudiante = id_estudiante
    estudiante.tipo_doc_id = tipo_doc
    estudiante.nombre_1 = nombre_1
    estudiante.nombre_2 = nombre_2
    estudiante.apellido_1 = apellido_1
    estudiante.apellido_2 = apellido_2
    estudiante.municipio_id = municipio
    estudiante.celular = celular
    estudiante.f_nacimiento = f_nacimiento

    estudiante.save()
    messages.success(request, '¡Estudiante actualizado correctamente!')
    return redirect('/')

def eliminarEstudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    messages.success(request, '¡Estudiante eliminado correctamente!')
    return redirect('/')

### Formaciones 
def formaciones(request):
    formacioneslistados = Formacion.objects.all()
    tiposformacioneslistados = Tiposformaciones.objects.all()
    messages.success(request, 'Formaciones listadas!')
    return render(request, "gestionFormaciones.html", {"formaciones": formacioneslistados, "tipoformacion":tiposformacioneslistados})

def registrarFormacion(request):
    nombre= request.POST['nombre']
    tipo_formacion = request.POST['tipo_formacion']
    horas = request.POST['horas']
    vigencia_dias = request.POST['vigencia_dias']

    formacion = Formacion.objects.create(nombre=nombre, tipo_formacion_id=tipo_formacion, horas=horas, vigencia_dias=vigencia_dias)
    messages.success(request, '¡Formación registrado correctamente!')
    return redirect('/formaciones/')
    
def edicionFormacion(request, id):
    formacion = Formacion.objects.get(id=id)
    tiposformacioneslistados = Tiposformaciones.objects.all()
    return render(request, "edicionFormacion.html", {"formacion": formacion, "tipoformacion":tiposformacioneslistados })

def editarFormacion(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    tipo_formacion = request.POST['tipo_formacion']
    horas = request.POST['horas']
    vigencia_dias = request.POST['vigencia_dias']

    formacion = Formacion.objects.get(id=id)
    formacion.nombre = nombre
    formacion.tipo_formacion_id = tipo_formacion
    formacion.horas = horas
    formacion.vigencia_dias = vigencia_dias

    formacion.save()
    messages.success(request, '¡Formación actualizada correctamente!')
    return redirect('/formaciones/')

def eliminarFormacion(request, id):
    formacion = Formacion.objects.get(id=id)
    formacion.delete()
    messages.success(request, '¡Formación eliminado correctamente!')
    return redirect('/formaciones/')


### Certificados 
def certificados(request):
    certificadoslistados = Certificado.objects.all()
    formacioneslistados = Formacion.objects.all()
    queryset = request.GET.get('buscar')
    if queryset:
        busquedaestudiante = Estudiante.objects.filter(id_estudiante=queryset)
        messages.success(request, 'Certificados listados!')
        return render(request, "gestionCertificados.html", {"certificados": certificadoslistados, "formaciones":formacioneslistados, "busqueda":busquedaestudiante})
    messages.success(request, 'Certificados listados!')
    return render(request, "gestionCertificados.html", {"certificados": certificadoslistados, "formaciones":formacioneslistados})

def random_id(lenght=10):
    MiCadena = string.ascii_letters + string.digits
    return "".join(random.choice(MiCadena)  for _ in range(lenght))

def registrarCertificado(request):
    id_estudiante = request.POST['id_estudiante']
    id_formacion = request.POST['id_formacion']
    fecha = request.POST['fecha']
    fecha_formateada = datetime.strptime(fecha, '%Y-%m-%d')
    consulta_formacion_fecha_vigencia = Formacion.objects.filter(id=id_formacion)
    resultado_fecha_vigencia = consulta_formacion_fecha_vigencia[0]
    fecha_vencimiento = fecha_formateada + timedelta(resultado_fecha_vigencia.vigencia_dias)
    
    while True:
        certificado_random_id = random_id()
        consulta_certificado = Certificado.objects.filter(id_certificado=certificado_random_id).exists()
        if consulta_certificado is False:
            id_certificado = certificado_random_id
            break
    

    certificado = Certificado.objects.create(id_certificado = id_certificado, id_formacion_id = id_formacion,id_estudiante_id=id_estudiante, fecha=fecha, fecha_vencimiento=fecha_vencimiento)
    messages.success(request, '¡Certificado registrado correctamente!')
    return redirect('/certificados/')

   

def eliminarCertificado(request, id_certificado):
    certificado = Certificado.objects.get(id_certificado=id_certificado)
    certificado.delete()
    messages.success(request, '¡Certificado eliminado correctamente!')
    return redirect('/certificados/')


