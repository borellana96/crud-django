from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm#, SignInForm
'''from .models import Tipo_proveedor'''

# Create your views here.
#def default(request):
#    return redirect('signin')

def signup(request, tipo_id):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        data = {
            'form': SignUpForm(),
        }
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid:
                form.save()
                if tipo_id == 1:
                    print('==== Se ha registrado un Cliente ====')
                    return render(request,'core/sidebarCliente.html', data)
                else:
                    print('==== Se ha registrado un Proveedor ====')
                    return render(request,'core/sidebarProveedor.html', data)      
                return redirect('home')
            data['form'] = form
        return render(request, 'register.html', data)

'''def signupComplete(request):
    if request.POST:
        tipo = Tipo_proveedor()
        tipo.usuario_id = request.POST.get('txtuser')
        tipo.save()
    return render(request, "registerComplete.html")'''

def signin(request, tipo_id):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context = {
        #    'form': SignInForm(),
            'tipo_user': tipo_id
        }
        if request.method == 'POST':
        #    form = SignInForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("==== Usuario aceptado ====")
                login(request, user)
                if tipo_id == 1:
                    print('Se ha logeado un Cliente')
                    return render(request,'core/sidebarCliente.html', context)
                else:
                    print('Se ha logeado un Proveedor')
                    return render(request,'core/sidebarProveedor.html', context)
            else:        
                messages.info(request, 'Usuario o contraseña incorrecto')
            #if request.user.is_authenticated:
            #    return redirect('crud/home')
        #    context['form'] = form
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')