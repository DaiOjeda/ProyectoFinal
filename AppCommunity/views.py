from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from AppCommunity.forms import GrupoFormulario
from AppCommunity.models import Grupo

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

def inicio(request):
    contexto = {
        'valor1': "este es un valor"
    }
    return render(request, 'index.html', contexto)
def grupo(request):
    grupos = Grupo.objects.all()
    contexto = {
        'object_list': grupos,
    }
    return render(request,'AppCommunity/grupo.html', contexto)

@login_required
def grupo_formulario(request):
    if request.method == 'POST':
        mi_formulario = GrupoFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            grupo1 = Grupo(
                camada=data.get('camada'),
                nombre_lider=data.get('nombre_lider'),
                apellido_lider=data.get('apellido_lider')
            )
            grupo1.save()

            return redirect('AppCommunityGrupo')
        contexto = {
            'form': GrupoFormulario(),
            'titulo_form': 'Grupos Formulario',
            'boton_envio': 'Crear'
        }
        return render(request, 'base/base_formulario.html', contexto)

@login_required
def editar_grupo(request, camada):
    grupo_editar = Grupo.objects.get(camada=camada)

    if request.method == 'POST':
        mi_formulario = GrupoFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            grupo_editar.camada = data.get('camada')
            grupo_editar.nombre_lider = data.get('nombre_lider')
            grupo_editar.apellido_lider = data.get('apellido_lider')

            grupo_editar.save()
            return redirect('AppCommunityInicio')

        contexto = {
            'form': GrupoFormulario(
                initial={
                    "camada": grupo_editar.camada,
                    "nombre_lider": grupo_editar.nombre_lider,
                    "apellido_lider": grupo_editar.apellido_lider
                }
            )
        }
        return render(request, 'base/base_formulario.html', contexto)

@login_required
def eliminar_grupo(request, camada):
    grupo_eliminar = Grupo.objects.get(camada=camada)
    grupo_eliminar.delete()

    messages.info(request, f"El {grupo_eliminar} fue eliminado")
    return redirect('AppCommunityGrupo')

#Mejoramos pagina de error
class Error404View(TemplateView):
    template_name = "AppCommunity/error_404.html"

class About(TemplateView):
    template_name = 'AppCommunity/about.html'

class GrupoList(LoginRequiredMixin, ListView):
    model = Grupo
    template_name='AppCommunity/curso.html'