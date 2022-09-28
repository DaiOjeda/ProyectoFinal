from django.urls import path
from AppCommunity.views import *

urlpatterns = [
    path('', inicio, name='AppCommunityInicio'),
    path('grupo/', grupo, name='AppCommunityGrupo'),
    path('grupo_formulario/', grupo_formulario, name='AppCommunityGrupoFormulario'),
    path('eliminar_grupo/<int:camada>', eliminar_grupo, name='AppCommunityEliminarGrupo'),
    path('editar_grupo/>int:camada>', editar_grupo, name='AppCommunityEditarGrupo')
]