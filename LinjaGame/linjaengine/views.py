from django.shortcuts import render,HttpResponse

# Create your views here.

def inicio (request):
    print('inicio')
    return HttpResponse('<h1>Hola mundo</h1>')