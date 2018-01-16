from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
#from . models import Post
from django.urls import reverse_lazy
# Create your views here.0
from .models import Usuari


from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm





#def index(request):

#    return render(request, 'main.html')
#def ind(request):

#        return render(request, 'main.html')
#def princ(request):
#    personas = [
#        { 'nombre' : 'Juanita', 'edad' : 20 },
#        { 'nombre' : 'Pepito', 'edad' : 28 },
#        { 'nombre' : 'Luisito', 'edad' : 10 }
#    ]
#    variables = {
#        'lista_personas' : personas
#    }
#    return render(request, 'principal.html', variables)



#def regist(request):

#    return render(request, 'registro.jsp')







def index(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    #else:


        #query = request.GET.get("q")
        #if query:

          # song_results = song_results.filter(
            #    Q(song_title__icontains=query)
            #).distinct()
    else:
            return render(request, 'index.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
            #return HttpResponse("Usuario o Contraseña incorrectos.")
    return render(request, 'login.html')




#def register(request):
#    form = UserForm(request.POST or None)
#    context = {
#        "form": form,
#    }
#    if form.is_valid():
#
#        datos = form.cleaned_data
#        nom = datos.get("nom")
#        corr = datos.get("corr")
#        cont = datos.get("cont")
#
#        reg = Usuari(nombre=nom, correos=corr, contrasena=cont)
#        print(nom, cont, corr)
#        reg.save()
#
#
#    return render(request, 'register.html', context)

def r1egister(request):


    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']

        #user.set_password(password)


        user1 = authenticate(username=username, email=email)

        if user1 is not None:
            if user1.is_active:
                login(request, user)


            else:
                return render(request, 'register.html', {'error_message': 'Your account has been disabled'})
        else:

            user.save()
    return render(request, 'register.html', context)
















def register(request):

    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']

        user.set_password(password)

        if request.method == "POST":
            username1 = request.POST['username']
            email1 = request.POST['email']
            user1 = authenticate(username=username1, email=email1)
            if user1 is not None:
                return render(request, 'register.html', {'error_message': 'Invalid register'})
            else:
                print(username, user1)
            #    if username != username1 and email !=email1:
            #        user.save()
            #        return render(request, 'login.html', {'error_message': 'Ya puedes Loguearte'})
            #    #return HttpResponse("Usuario o Contraseña incorrectos.")
            #    else:
            #        return render(request, 'register.html', {'error_message': 'Usuario o correo ya registrados'})

                #if user1 == username1 or email == email1:
                #    return render(request, 'register.html', {'error_message': 'Usuario o correo ya registrados'})
                #else:

                user.save()
                return render(request, 'login.html', {'error_message': 'Ya puedes Loguearte'})








    context = {
        "form": form,
    }
    return render(request, 'register.html', context)
