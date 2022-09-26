from django.urls import path
from AppCommunity.views import *

urlpatterns = [
    path('', inicio, name='AppCommunityInicio'),
    path('grupo/', grupo, name='AppCommunityGrupo'),
    path('eliminar_grupo/', eliminar_grupo, name='AppCommunityEliminarGrupo'),
    path('editar_grupo/', editar_grupo, name='AppCommunityEditarGrupo')
]