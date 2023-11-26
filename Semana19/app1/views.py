from django.shortcuts import render
from django.shortcuts import render,redirect
from .formularios.registerform import NewUserForm
from .formularios.loginform import LoginForm
from django.http import HttpResponseRedirect
from .models import Productos,Proveedores
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, HttpResponseRedirect
from .formularios.registerform import NewUserForm

def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "Reg_user.html", {"form": formulario})
    else:
        formulario = NewUserForm()
        return render(request, "Reg_user.html", {"form": formulario})

def index(request):
    return render(request, 'index.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    


def lista_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

# app1/views.py
from .forms import ProveedorForm

def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': form})

   
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html', {'user': request.user})

@login_required(login_url='login')
def index(request):
    es_estudiante = request.user.groups.filter(name='Estudiante').exists() 
    es_admin = request.user.is_staff 
    if es_estudiante or es_admin:
        return render(request, 'index.html', {'user': request.user, 'es_estudiante': es_estudiante,'es_admin':es_admin})