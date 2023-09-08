from django.shortcuts import redirect, render
from django.contrib.auth import logout

def inicio_admin(request):
    titulo ="Inicio"
    context={
        "titulo": titulo
    }
    return render(request, 'index-admin.html', context)
    

def logout_user(request):
    logout(request)
    return redirect('inicio')