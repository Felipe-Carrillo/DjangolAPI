from django.contrib import admin
from django.urls import path 
from api.login.login_view import (
    login_view, registrar_views, recuperar_views, salir_view,
)
from api.home.home_view import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('salir/', salir_view, name='salir'),
    path('registrar/', registrar_views, name='registrar'),
    path('recuperar/', recuperar_views, name='recuperar'),
    path('', home_view, name='home'),  # Ruta para la página de inicio
]

