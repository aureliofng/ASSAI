from django.urls import path
from django.views import View
from . import views

urlpatterns = [

    # Estudiantes
    path('', views.home),
    path('registrarEstudiante/', views.registrarEstudiante),
    path('eliminarEstudiante/<id>', views.eliminarEstudiante),
    path('editarEstudiante/', views.editarEstudiante),
    path('edicionEstudiante/<id>', views.edicionEstudiante),

    # Formaciones
    path('formaciones/', views.formaciones),
    path('registrarFormacion/', views.registrarFormacion),
    path('edicionFormacion/<id>', views.edicionFormacion),
    path('editarFormacion/', views.editarFormacion),
    path('eliminarFormacion/<id>', views.eliminarFormacion),
    path('municipios/', views.municipios),

    # Certificados
    path('certificados/', views.certificados),    
    path('registrarCertificado/', views.registrarCertificado),
    path('eliminarCertificado/<id_certificado>', views.eliminarCertificado),
    path('descargarCertificado/pdf/<id_certificado>', views.docpdf),
    path('descargarCertificado/', views.docpdf),

    path('pdf/<id_certificado>', views.pdfv),
    path('pdf2/<id_certificado>', views.pdf_ver),   
]
