"""ProyectoJuridico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from mainApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView

import mainApp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('archivo/', views.archivo, name='archivo'),
    path('redenciones/', views.redenciones, name='redenciones'),
    path('libertades/', views.libertades, name ='libertades'),
    path('72h/', views.A_72h, name='72h'),
    path('tutelas/', views.tutelas, name='tutelas'),
    path('prueba/', views.prueba,name='prueba'),
    path('guardar_funci/', views.guardar_funci, name='guardar_funci'),
    path('guardar_area/', views.guardar_area, name='guardar_area'),
    path('seccion/', views.seccion, name ='seccion'),
    path('guardar_tramite/', views.guardar_tramiteliber, name ='guardar_tramite'),
    path('guardar_tramitereden/', views.guardar_tramitereden, name ='guardar_tramitereden'),
    path('guardar_tramitere72h/', views.guardar_tramitere72h, name ='guardar_tramitere72h'),
    path('guardar_tramitetutela/', views.guardar_tramitetutela, name ='guardar_tramitetutela'),
    path('guardar_tramitepreshv/', views.guardar_tramitepreshv, name ='guardar_tramitepreshv'),
    path('asesor/', views.buscarx, name ='asesor'),
    path('cambiar_estado/', views.cambiarestado, name ='cambiar_estado'),
    path('eliminar/', views.eliminar, name ='eliminar'),
    path('eliminar72/', views.eliminar72, name ='eliminar72'),
    path('eliminarreden/', views.eliminarreden, name ='eliminarreden'),
    path('eliminartutela/', views.eliminartutela, name ='eliminartutela'),
    path('devolucion/', views.devolucion, name ='devolucion'),
    path('pruebapepe/', views.pruebapepe, name ='pruebapepe'),
    path('',LoginView.as_view(template_name='index.html'),name='login'),
    path('prueba/',views.pruebapepe,name='pepe')
    

    
]

urlpatterns += staticfiles_urlpatterns()
