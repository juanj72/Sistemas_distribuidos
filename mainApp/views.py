from django.core.checks import messages
from django.shortcuts import redirect, render, HttpResponse
from mainApp.models import *
from django.contrib import messages
from datetime import date
from django.db.models import Q
from django.views.generic import ListView


# Create your views here.

def cambiarestado(request):
    id = request.GET['id']
    print(id)
    h = PPLxTramites.objects.filter(id=id).update(id_estadotramite=id)
    print(h)
    

    return redirect('libertades')

def capturar(request):
    id = request.GET['ide']
    print(id)
    
    

    return (id)

def mostrarppls():
    ppls= PPL.objects.all()

    return(ppls)

    ######TRAMITES DE PRESTAMO HV ##########
def guardar_tramitepreshv(request):

    if request.method == 'POST':
        nui = request.POST['ppl']
        funcionario = request.POST['funcionarios']
        id_ppl = encontrar_id_ppl(nui)
        id_funcionario = encontrar_id_funcionariohv(funcionario)
        descripcion = request.POST['descrip_pres']
        fecha_prestamo = request.POST['fecha_pres']
        
       
        

        tramite_preshv = Prestamo_hv(

            id_ppl =  id_ppl,
            id_funcionario = id_funcionario,
            descripcion = descripcion,
            fecha_prestamo = fecha_prestamo,
            
           
            
        )

        tramite_preshv.save()

        messages.success(request,f"ppl{id_ppl}")
    else:
        messages.error(request,f"no se guardo el tramite")
        
    

    return redirect('archivo')

def archivo(request):
    ppls = mostrarppls()
    funcionarios = mostrarfuncionarios()
    prestamos = mostrarprestamos()

    return render(request, "vista_archivo.html",{
        
        'funcionarios'       :funcionarios,
        'ppls'           : ppls,
        'prestamos'      : prestamos,

    })

def devolucion(request):
    id = request.GET['id']
    hoy = date.today()
    h = Prestamo_hv.objects.filter(id=id).update(fecha_devolucion=hoy)
    print(h)
    

    return redirect('archivo')


    ###### FIN TRAMITES DE PRESTAMO HV ##########

def buscarx(request):
    busqueda = request.GET.get("buscar")
    tramites = PPLxTramites.objects.all()

    if busqueda:
        tramites = PPLxTramites.objects.filter(
            Q(id_ppl__nombre__icontains = busqueda)|
            Q(id_ppl__nui__icontains = busqueda)|
            Q(id_funcionario__nombre_funci__icontains = busqueda)|
            Q(id_tipotramite__nombre_tipo__icontains = busqueda)|
            Q(id_estadotramite__estado_tramite__icontains = busqueda)|
            Q(fecha_peticion__contains = busqueda)|
            Q(fase_72h__contains = busqueda)|
            Q(visitadomi_72h__contains = busqueda)|
            Q(antecedentes_72h__contains = busqueda)|
            Q(radi_oficio_libertades__contains = busqueda)|
            Q(autoridad_tutela__contains = busqueda)|
            Q(asunto_tutela__contains = busqueda)|
            Q(oficio_envio_tutela__contains = busqueda)|
            Q(observa_desa_tutela__contains = busqueda)|
            Q(observaciones__contains = busqueda)|
            Q(fecha_envio_tramite__contains = busqueda)
            
        ).distinct()
        
    

    return render(request, 'vista_asesor.html', {'tramites': tramites})




    ######TRAMITES DE TUTELAS ##########
def guardar_tramitetutela(request):

    if request.method == 'POST':
        area = '5'
        estado = '2'
        nui = request.POST['ppl']
        id_ppl = encontrar_id_ppl(nui)
        id_funcionario = encontrar_id_funcionario(area)
        id_tipotramite = encontrar_id_tipo(area)
        id_estadotramite = encontrar_estado(estado)
        fecha_peticion = request.POST['fecha_tutela']
        autoridad_tutela = request.POST['autoridad']
        asunto_tutela = request.POST['anteceppl']
        oficio_envio_tutela = request.POST['oficioenvi_tute']
        radi_oficio_libertades = request.POST['radicadottla']
       
        

        tramite_tute = PPLxTramites(

            id_ppl = id_ppl,
            id_funcionario =  id_funcionario,
            id_tipotramite = id_tipotramite,
            id_estadotramite = id_estadotramite,
            fecha_peticion = fecha_peticion,
            autoridad_tutela = autoridad_tutela,
            asunto_tutela = asunto_tutela,
            oficio_envio_tutela = oficio_envio_tutela,
            radi_oficio_libertades = radi_oficio_libertades
           
            
        )

        tramite_tute.save()

        messages.success(request,f"ppl{id_ppl}")
    else:
        messages.error(request,f"no se guardo el tramite")
        
    

    return redirect('tutelas')

def mostrarxtramitestute():

   
   tute = PPLxTramites.objects.filter(id_tipotramite_id=4)

   return(tute)

def tutelas(request):
    ppls = mostrarppls()
    tramites = mostrarxtramitestute()
    

    return render(request, "vista_tutelas.html",{
        
        'tramites'       :tramites,
        'ppls'           : ppls,

    })

    ######FIN TRAMITES DE TUTELAS ##########

    ######TRAMITES DE 72H ##########

def guardar_tramitere72h(request):

    if request.method == 'POST':
        area = '2'
        estado = '2'
        nui = request.POST['ppl']
        id_ppl = encontrar_id_ppl(nui)
        id_funcionario = encontrar_id_funcionario(area)
        id_tipotramite = encontrar_id_tipo(area)
        id_estadotramite = encontrar_estado(estado)
        fecha_peticion = request.POST['fecha_permiso']
        observaciones = request.POST['descrip_pres']
        fecha_envio_tramite= request.POST['fechaev_permiso']
        fase_72h = request.POST['faseppl']
        visitadomi_72h = request.POST['visitappl']
        antecedentes_72h = request.POST['anteceppl']

        tramite_72h = PPLxTramites(

            id_ppl = id_ppl,
            id_funcionario =  id_funcionario,
            id_tipotramite = id_tipotramite,
            id_estadotramite = id_estadotramite,
            fecha_peticion = fecha_peticion,
            observaciones = observaciones,
            fecha_envio_tramite= fecha_envio_tramite,
            fase_72h = fase_72h,
            visitadomi_72h = visitadomi_72h,
            antecedentes_72h = antecedentes_72h
            
        )

        tramite_72h.save()

        messages.success(request,f"ppl{id_ppl}")
    else:
        messages.error(request,f"no se guardo el tramite")
        
    

    return redirect('72h')

def mostrarxtramites72():

   
   per72 = PPLxTramites.objects.filter(id_tipotramite_id=3)

   return(per72)

def A_72h(request):
    ppls = mostrarppls()
    tramites = mostrarxtramites72()
    

    return render(request, "vista_72h.html",{
        
        'tramites'       :tramites,
        'ppls'           : ppls,
        

    })

    ######FIN TRAMITES DE 72H ##########





    ######TRAMITES DE REDENCIONES ##########

def guardar_tramitereden(request):

    if request.method == 'POST':
        area = '4'
        estado = '2'
        nui = request.POST['ppl']
        id_ppl = encontrar_id_ppl(nui)
        id_funcionario = encontrar_id_funcionario(area)
        id_tipotramite = encontrar_id_tipo(area)
        id_estadotramite = encontrar_estado(estado)
        fecha_peticion = request.POST['fechadp_reden']
        observaciones = request.POST['descrip_pres']
        fecha_envio_tramite= request.POST['fechaej_reden']

        tramite_reden = PPLxTramites(

            id_ppl = id_ppl,
            id_funcionario =  id_funcionario,
            id_tipotramite = id_tipotramite,
            id_estadotramite = id_estadotramite,
            fecha_peticion = fecha_peticion,
            observaciones = observaciones,
            fecha_envio_tramite= fecha_envio_tramite
            
        )

        tramite_reden.save()

        messages.success(request,f"ppl{id_ppl}")
    else:
        messages.error(request,f"no se guardo el tramite")
        
    

    return redirect('redenciones')

def mostrarxtramitesreden():

   
   reden = PPLxTramites.objects.filter(id_tipotramite_id=2)

   return(reden)


def redenciones(request):
    ppls = mostrarppls()
    tramites = mostrarxtramitesreden()
    

    return render(request, "vista_reden.html",{
        
        'tramites'       :tramites,
        'ppls'           : ppls,
        

    })

    ######FIN TRAMITES DE REDENCIONES ##########



    ######TRAMITES DE LIBERTADES ##########

def mostrarpplsxtramites():
    tramites= PPLxTramites.objects.all()

    return(tramites)

def mostrarestados():
    estados= Estado_tramites.objects.all()

    return(estados)

def mostrarfuncionarios():
    funcionarios= Funcionario.objects.all()

    return(funcionarios)

def mostrarprestamos():
    prestamos= Prestamo_hv.objects.all()

    return(prestamos)


def mostrarxtramitesliber():

   #liber = PPLxTramites.objects.filter(id_tipotramite = '4')
   libert = PPLxTramites.objects.filter(id_tipotramite_id=1)

   return(libert)




def libertades(request):
    ppls = mostrarppls()
    tramites = mostrarxtramitesliber()
    estados = mostrarestados()
    

    return render(request, "vista_liber.html",{
        
        'tramites'       :tramites,
        'estados'        : estados,
        'ppls'           : ppls,
        

    })





def guardar_tramiteliber(request):

    if request.method == 'POST':
        area = '3'
        estado = '2'
        nui = request.POST['ppl']
        id_ppl = encontrar_id_ppl(nui)
        id_funcionario = encontrar_id_funcionario(area)
        id_tipotramite = encontrar_id_tipo(area)
        id_estadotramite = encontrar_estado(estado)
        fecha_peticion = request.POST['fecha_peti']
        radi_oficio_libertades = request.POST['no_oficio']
        observaciones = request.POST['observa']
        fecha_envio_tramite= request.POST['fecha_juz']

        tramite_li = PPLxTramites(

            id_ppl = id_ppl,
            id_funcionario =  id_funcionario,
            id_tipotramite = id_tipotramite,
            id_estadotramite = id_estadotramite,
            fecha_peticion = fecha_peticion,
            radi_oficio_libertades =  radi_oficio_libertades,
            observaciones = observaciones,
            fecha_envio_tramite= fecha_envio_tramite
            
        )

        tramite_li.save()

        messages.success(request,f"ppl{id_ppl}")
    else:
        messages.error(request,f"no se guardo el tramite")
        
    
    return redirect('libertades')

def encontrar_id_ppl (nui):
    
    #ppl = PPL.objects.only('id').get(nui=nui).id
    ppl= PPL.objects.all().get(nui=nui)
    
    return ppl

def encontrar_id_funcionario (area):
    
    #funci = Funcionario.objects.only('id').get(id_area_id=area).id
    funci = Funcionario.objects.all().get(id_area_id=area)
    
    return funci

def encontrar_prestamo (id):
    
    #funci = Funcionario.objects.only('id').get(id_area_id=area).id
    prestamo = Prestamo_hv.objects.all().get(id=id)
    
    return prestamo

def encontrar_id_tipo(area):
    
    #tipo = Tipo_tramite.objects.only('id').get(id_area_id=area).id
    tipo = Tipo_tramite.objects.all().get(id_area_id=area)
    
    return tipo

def encontrar_id_funcionariohv(id):
    
    #tipo = Tipo_tramite.objects.only('id').get(id_area_id=area).id
    funcionario = Funcionario.objects.all().get(id=id)
    
    return funcionario

def encontrar_estado(estado):
    
    #tipo = Tipo_tramite.objects.only('id').get(id_area_id=area).id
    esatdo = Estado_tramites.objects.all().get(id=estado)
    
    return esatdo

 ###### FIN TRAMITES DE LIBERTADES ##########








def index(request):
    return render(request, "index.html")



def prueba(request):
    return render(request, "prueba.html")


def guardar_funci(request):

    funcionario = Funcionario(
        id_area=1,
        documento_funci = 17087678,
        nombre_funci = 'Andrea',
        apellidos_funci = 'Campos',
        cargo = 'Administrador',
        genero_funci = 'Femenino',
        passw = 17087678
    )

    funcionario.save()
    return HttpResponse(f'dato almacenado: {funcionario.nombre_funci}')

def guardar_area(request):

    area = Area(
        nombre_area = 'Tutelas',
        descripcion_area = 'Realizar seguimiento y control de tutelas'

    )

    area.save()
    return HttpResponse(f'dato almacenado: {area.nombre_area}')

def seccion(request):
    if request.method == 'POST':
        documento= request.POST['usuario']
        password = request.POST['pass']
        
        funci_docu = Funcionario.documento_funci,
        funci_pass = Funcionario.passw,
        funci_area = Funcionario.id_area,

        if (documento== funci_docu and password== funci_pass):
            if (funci_area == 1):
                return render(request, "vista_archivo.html")
            elif(funci_area==2):
                return render(request, "vista_72h.html")
            elif(funci_area==3):
                return render(request, "vista_liber.html")
            elif(funci_area==4):
                return render(request, "vista_reden.html")
            elif(funci_area==5):
                return render(request, "vista_tutelas.html")
        else:
            
            return render(request, "index.html")
    else:
        return render(request, "index.html")
    
    return redirect('')


        