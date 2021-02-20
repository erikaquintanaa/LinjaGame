from django.shortcuts import render,HttpResponse

# Create your views here.

def layout (request):
    print('inicio')
    return render(request,'main.html')

def init_game (request):
    return render(request,'init-game.html')
