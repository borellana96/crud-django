from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.http import JsonResponse
from .forms import ProductForm
from .models import Product

# Create your views here.
def default(request):
    return redirect('home')

def home(request):
    return render(request, 'core/home.html')

def send_email(request):
    nombre = request.POST.get('nombre') #Se obtiene el nombre del producto
    context = { 'nombre' : nombre }
    
    template = get_template('core/email.html')  #Muestra el template que se enviará al correo
    content = template.render(context)          #Manda al template el context

    mensaje = EmailMultiAlternatives(   #Configuración del correo
        'Un correo de prueba',  #Nombre del email
        'asunto',               #Asunto
        settings.EMAIL_HOST_USER,       #El que envía
        ['brian.orellana@unmsm.edu.pe'] #Destinatario
    )
    mensaje.attach_alternative(content, 'text/html')
    mensaje.send()
    print('Enviado')

def manage(request):
    data = {
        'form': ProductForm(),
        'enviado': False
    }
    return render(request, 'core/manageProduct.html', data)

def create(request):
    data = {
        'form': ProductForm(),
        'enviado': False
    }
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            data['mensaje']='Se ha enviado tu mensaje correctamente!'
            data['enviado']=True
            #send_email(request)
        data['form'] = form
    return render(request, 'core/createProduct.html', data)

def read(request):
    producto = Product.objects.all()
    context = {'productos': producto} #productos es el nombre de la lista que estará en el HTML
    return render(request, 'core/readProduct.html', context) #el context es el que se envía al html

def update(request, id):
    producto = Product.objects.get(id=id)
    if request.method == 'GET':
        form = ProductForm(instance = producto)
    else:
        form = ProductForm(request.POST, instance = producto)
        if form.is_valid:
            form.save()
        return redirect('home')
    return render(request, 'core/createProduct.html',{'form': form})

def delete(request, id):
    producto = Product.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('home')
    return render(request, 'core/deleteProduct.html', {'producto': producto})

#@login_required(login_url='signin')
def vender(request):
    if request.user.is_authenticated:
        return render(request, 'core/vender.html')
    else:
        return redirect('signin', tipo_id=2)

def contact(request):
    data={
        
    }
    if request.method == 'POST':
        asunto = request.POST.get('asunto')
        descripcion = request.POST.get('descripcion')
        if not asunto:
            data['asuntoMessage'] = 'Falta llenar este campo'
        elif asunto == 'repetido':
            data['asuntoMessage'] = 'Este asunto ya está ocupado'

        if not descripcion:
            data['descripcionMessage'] = 'Falta llenar este campo'
        elif descripcion == 'repetido':
            data['descripcionMessage'] = 'Este descripcion ya está ocupado'

        return JsonResponse(data, safe=False)
    return render(request, 'core/contact.html', data)