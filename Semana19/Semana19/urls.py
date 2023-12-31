"""
URL configuration for Semana19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views as ap1v
from django.urls import path
from app1.views import lista_proveedores, agregar_proveedor,lista_productos, agregar_producto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ap1v.index,name="home"),
    path('login/', ap1v.iniciar_sesion,name="login"),
    path('logout/', ap1v.cerrar_sesion, name='logout'),
    path('registro/', ap1v.reg_user),
    path('proveedores/', lista_proveedores, name='lista_proveedores'),
    path('agregar_proveedor/', agregar_proveedor, name='agregar_proveedor'),
    path('productos/', lista_productos, name='lista_productos'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
]