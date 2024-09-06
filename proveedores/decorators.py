from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def solo_supervisores(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.perfil.rol == 'supervisor':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden('Acceso Denegado')
    return wrapper_func