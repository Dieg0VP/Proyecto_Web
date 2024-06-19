from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Catalogo, Producto
from .forms import ProductoForm

# Create your views here.
def home(request):
    is_superuser = request.user.is_superuser
    data={'is_superuser': is_superuser}
    return render(request,'tienda/index.html',data)

@login_required
def index(request):
    is_superuser = request.user.is_superuser
    data={'is_superuser': is_superuser}
    return render(request,'tienda/indexLogin.html',data)

def registro(request):
    context = {}
    return render(request, 'tienda/registro.html', context)


def catalogo(request):
    is_superuser = request.user.is_superuser
    catalogos = Catalogo.objects.all()
    selected_catalogo = request.GET.get('catalogo')  # Obtener el valor del parámetro 'catalogo' de la URL

    if selected_catalogo:
        productos = Producto.objects.filter(nombreCa_id=selected_catalogo)
    else:
        productos = Producto.objects.all()

    context = {"productos": productos, "catalogos": catalogos, "selected_catalogo": selected_catalogo, "is_superuser": is_superuser}
    return render(request, 'tienda/catalogo.html', context)

def contacto(request):
    is_superuser = request.user.is_superuser
    data={'is_superuser': is_superuser}
    return render(request, 'tienda/contacto.html', data)

def agregar_producto(request):
    is_superuser = request.user.is_superuser
    data= {'form': ProductoForm(),'is_superuser': is_superuser}

    if request.method =='POST':
        formulario=ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "guardado corretamente"

        else:
            data['form']=formulario
    return render( request,'tienda/producto/agregar.html',data)

@login_required
def listar_producto(request):
    is_superuser = request.user.is_superuser
    productos= Producto.objects.all()
    data={'productos':productos,'is_superuser': is_superuser}
    return render(request,'tienda/producto/listar.html',data)

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    data = {'form': ProductoForm(instance=producto)}
    if request.method =='POST':
        formulario = ProductoForm(data=request.POST,instance=producto,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Producto modificado con exito"
            return redirect(to="listar-producto")
        data['form']=formulario

    return render(request,'tienda/producto/modificar.html',data)

def eliminar_producto(request, id):
    producto= get_object_or_404(Producto,id_producto=id)
    producto.delete()
    return redirect(to="listar-producto")

def salir(request):
    logout(request)
    return redirect('/')

def login(request):
    login(request)
    return redirect('/')

def catalogo_general(request):
    is_superuser = request.user.is_superuser
    catalogos = Catalogo.objects.all()
    context = {"catalogos": catalogos,'is_superuser': is_superuser}
    return render(request, 'tienda/catalogo_general.html', context)


def catalogo_desc(request, catalogo_id):
    is_superuser = request.user.is_superuser
    catalogo = get_object_or_404(Catalogo, pk=catalogo_id)
    productos = Producto.objects.filter(nombreCa=catalogo)
    context = {"catalogo": catalogo, "productos": productos,'is_superuser': is_superuser}
    return render(request, 'tienda/catalogo_desc.html', context)
