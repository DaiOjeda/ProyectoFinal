from django.urls import path
from django.contrib.auth.views import LogoutView
from UserCommunity.views import *


urlpatterns = [
    path('login', login_request, name='UserCommunityLogin'),
    path('registro/', register, name='UserCommunityRegister'),
    path('logout/', LogoutView.as_view(template_name='UserCommunity/logout.html'), name='UserCommunityLogout'),
    path('editar/', editar_usuario, name='UserCommunityEditar'),
    path('avatar/', upload_avatar, name='UserCoderAvatar'),
]