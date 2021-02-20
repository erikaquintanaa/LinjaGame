from django.shortcuts import render,HttpResponse

# Create your views here.

def index (request):
    print('inicio')
    return render(request,'index.html')