from django.shortcuts import render
from django.shortcuts import render,redirect
from .formularios.registerform import NewUserForm
from .formularios.loginform import LoginForm
from django.http import HttpResponseRedirect
from .models import Productos,Proveedores
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect("/")
    else:
        formulario = NewUserForm()
        render(request,"Reg_user.html",{"form":formulario})
        return
   
    
def index(request):
    return render(request, 'index.html')
