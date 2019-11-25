from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, UserForm

#import of fundation register 
from django.contrib.auth import login as do_login
from django.contrib.auth.models import Group

#registro de usuarios
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
      form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#Editar perfiles usuarios
def edit_profile(request, password=None):
  if request.method == 'POST':
    form = UserForm(request.POST, instance=request.user)

    if form.is_valid():
       form.save()
       return redirect('accept_profile')
  else:
      form = UserForm(instance=request.user)
      args={'form': form}

      return render(request, 'edit_profile.html', {'form': form})


#registro para las fundaciones
def register(request):
    return render(request, "register.html")

#registro de fundaciones
def register(request):
    #Creamos el formulario de autentificación vacio
    form = SignUpForm()
    if request.method == "POST":
        #añadimos los datos recibidos al formulario
        form = SignUpForm(data=request.POST)
        #si el formulario es valido..      
        if form.is_valid():

            #creamos la nueva cuenta de usuario
            fundaciones = form.save()
            #Guardar usuario en grupo fundaciones
            g = Group.objects.get(name='fundaciones') 
            g.user_set.add(fundaciones)
            #si el usuario se crea correctamnte
            if fundaciones is not None:
                #hacemos el login manualmente
                do_login(request, fundaciones)
                #y le redireccionamos a la portada
                return redirect('/')
    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    #si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})


