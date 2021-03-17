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
    print('Ficha ----> ',request.POST['contenido'])
    print('Id Ficha ----> ',request.POST['id'])
    print('Numero en fila ----> ',request.POST['Num_Peones_Fila'])
    print()

    return HttpResponse(respuestaBien)
