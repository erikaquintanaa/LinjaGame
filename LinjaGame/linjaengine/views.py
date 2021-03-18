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

    print()
    print('Cantidad en fila 1 ----> ',request.POST['fila1'])
    print('Cantidad en fila 2 ----> ',request.POST['fila2'])
    print('Cantidad en fila 3 ----> ',request.POST['fila3'])
    print('Cantidad en fila 4 ----> ',request.POST['fila4'])
    print('Cantidad en fila 5 ----> ',request.POST['fila5'])
    print('Cantidad en fila 6 ----> ',request.POST['fila6'])
    print('Cantidad en fila 7 ----> ',request.POST['fila7'])
    print('Cantidad en fila 8 ----> ',request.POST['fila8'])
    print()
    print('Cantidad en fila 1 ----> Hay ',request.POST['fila1'],' peones que equivalen a ',ValoresTotalesFila(request.POST['fila1'],'1'),' puntos')
    print('Cantidad en fila 2 ----> Hay ',request.POST['fila2'],' peones que equivalen a ',ValoresTotalesFila(request.POST['fila2'],'2'),' puntos')
    print('Cantidad en fila 3 ----> Hay ',request.POST['fila3'],' peones que equivalen a ',ValoresTotalesFila(request.POST['fila3'],'3'),' puntos')
    print('Cantidad en fila 4 ----> Hay ',request.POST['fila4'],' peones que equivalen a ',ValoresTotalesFila(request.POST['fila4'],'4'),' puntos')
    print('Cantidad en fila 5 ----> Hay ',request.POST['fila5'],' peones que equivalen a ',ValoresTotalesFila(request.POST['fila5'],'4'),' puntos')
    print('Cantidad en fila 6 ----> Hay ',request.POST['fila6'],' peones que equivalen a ',ValoresTotalesFila(request.POST['fila6'],'3'),' puntos')
    print('Cantidad en fila 7 ----> Hay ',request.POST['fila7'],' peones que equivalen a ',ValoresTotalesFila(request.POST['fila7'],'2'),' puntos')
    print('Cantidad en fila 8 ----> Hay ',request.POST['fila8'],' peones que equivalen a ',ValoresTotalesFila(request.POST['fila8'],'1'),' puntos')



    return HttpResponse(respuestaBien)

def ValoresTotalesFila(num,fila):
    if fila == '1':
        result=int(num)*5

    if fila == '2':
        result=int(num)*3

    if fila == '3':
        result=int(num)*2

    if fila == '4':
        result=int(num)*1


    return result


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
