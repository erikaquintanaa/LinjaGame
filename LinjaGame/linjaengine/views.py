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
    print('request',request.POST.q('totalTodos'))
    """ print('Tabla ----> ',request.POST['tablaPeones'])
    print()
    print('Ficha ----> ',request.POST['contenidoPeon'])
    print('Id Ficha ----> ',request.POST['id'])
    print()
    movPeon2 = PeonesMov2(request.POST['Num_Peones_Fila'])
    print(movPeon2)
    print()
    tb= analizarTablaPeones(request.POST['tablaPeones'])
    print('Cantidad en totalTodos ----> Hay ',request.POST['totalTodos'])


    print()
    print('Cantidad en fila 1 ----> Hay ',request.POST['fila1Negro'],' peones negros que equivalen a ',ValoresTotalesFila(request.POST['fila1Negro'],'0'),' puntos')
    print('Cantidad en fila 2 ----> Hay ',request.POST['fila2Negro'],' peones negros que equivalen a ',ValoresTotalesFila(request.POST['fila2Negro'],'0'),' puntos')
    print('Cantidad en fila 3 ----> Hay ',request.POST['fila3Negro'],' peones negros que equivalen a ',ValoresTotalesFila(request.POST['fila3Negro'],'0'),' puntos')
    print('Cantidad en fila 4 ----> Hay ',request.POST['fila4Negro'],' peones negros que equivalen a ',ValoresTotalesFila(request.POST['fila4Negro'],'0'),' puntos')
    print('Cantidad en fila 5 ----> Hay ',request.POST['fila5Negro'],' peones negros que equivalen a ',ValoresTotalesFila(request.POST['fila5Negro'],'4'),' puntos')
    print('Cantidad en fila 6 ----> Hay ',request.POST['fila6Negro'],' peones negros que equivalen a ',ValoresTotalesFila(request.POST['fila6Negro'],'3'),' puntos')
    print('Cantidad en fila 7 ----> Hay ',request.POST['fila7Negro'],' peones negros que equivalen a ',ValoresTotalesFila(request.POST['fila7Negro'],'2'),' puntos')
    print('Cantidad en fila 8 ----> Hay ',request.POST['fila8Negro'],' peones negros que equivalen a ',ValoresTotalesFila(request.POST['fila8Negro'],'1'),' puntos')

    print()
    print('Cantidad en fila 1 ----> Hay ',request.POST['fila1Rojo'],' peones rojos que equivalen a ',ValoresTotalesFila(request.POST['fila1Rojo'],'1'),' puntos')
    print('Cantidad en fila 2 ----> Hay ',request.POST['fila2Rojo'],' peones rojos que equivalen a ',ValoresTotalesFila(request.POST['fila2Rojo'],'2'),' puntos')
    print('Cantidad en fila 3 ----> Hay ',request.POST['fila3Rojo'],' peones rojos que equivalen a ',ValoresTotalesFila(request.POST['fila3Rojo'],'3'),' puntos')
    print('Cantidad en fila 4 ----> Hay ',request.POST['fila4Rojo'],' peones rojos que equivalen a ',ValoresTotalesFila(request.POST['fila4Rojo'],'4'),' puntos')
    print('Cantidad en fila 5 ----> Hay ',request.POST['fila5Rojo'],' peones rojos que equivalen a ',ValoresTotalesFila(request.POST['fila5Rojo'],'0'),' puntos')
    print('Cantidad en fila 6 ----> Hay ',request.POST['fila6Rojo'],' peones rojos que equivalen a ',ValoresTotalesFila(request.POST['fila6Rojo'],'0'),' puntos')
    print('Cantidad en fila 7 ----> Hay ',request.POST['fila7Rojo'],' peones rojos que equivalen a ',ValoresTotalesFila(request.POST['fila7Rojo'],'0'),' puntos')
    print('Cantidad en fila 8 ----> Hay ',request.POST['fila8Rojo'],' peones rojos que equivalen a ',ValoresTotalesFila(request.POST['fila8Rojo'],'0'),' puntos')
 """
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

    if fila == '0':
        result=int(num)*0

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
