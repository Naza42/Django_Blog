from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

    
def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def login(request):
    return render(request, 'usuarios/login.html')

def registro(request):
    return render(request, 'usuarios/registro.html')
