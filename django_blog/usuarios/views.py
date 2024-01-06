from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from .forms import RegistroForm
from django.urls import reverse_lazy
from .models import Usuario

#Vista para el inicio de sesion
def user_login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') #Redireccion a la pagina de inicio despues del logeo
        else:
            messages.error(request, 'Usuario o contraseña invalido, intente nuevamente')

        return render(request, 'usuarios/login.html')


#Vista para el cierre de sesion
def user_logout(request):
        logout(request)
        return redirect('login')


def Registro(request):
    if request.method == 'POST':
        form = RegistroForm()
        return  render(request, '/usuarios/registro.html', {'form': form})