from django.shortcuts import render,HttpResponse
import json

# Create your views here.

respuestaBien = '{"status":0,"message":"OK"}'

respuestaMal = '{"status":1,"message":"Error desde back..."}'

def layout (request):
    print('inicio')
    return render(request,'main.html')

def init_game (request):
    return render(request,'init-game.html')

def engine_game (request):
    print()
    print('Tabla ----> ',request.POST['tablaPeones'])
    print()
    print('Ficha ----> ',request.POST['contenidoPeon'])
    print('Id Ficha ----> ',request.POST['id'])
    #print('Numero en fila ----> ',request.POST['Num_Peones_Fila'])
    print()
    movPeon2 = PeonesMov2(request.POST['Num_Peones_Fila'])
    print(movPeon2)
    print()
    tb= analizarTablaPeones(request.POST['tablaPeones'])


    return HttpResponse(respuestaBien)


def PeonesMov2(text):
    return 'La cantidad de saltos para el peon 2 son de '+text


def analizarTablaPeones(tabla):
    dataCont = len(tabla)
    data = tabla
    #print(data)
    indice = 0
    while indice < len(data):

        letra = data[indice:indice+28]
        if(letra == "inicial filaNegra1 filaRoja8"):
            print(letra)

        indice += 1

    return tabla
