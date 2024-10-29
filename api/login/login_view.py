from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import logout

@csrf_protect
def login_view(request):
    """Vista para el inicio de sesión"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Intentar autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si las credenciales son válidas, iniciar sesión
            login(request, user)
            return redirect('home')
        else:
            # Si las credenciales son inválidas, mostrar mensaje de error
            messages.error(request, 'Credenciales inválidas')  # Mensaje de error

    # Si no es POST o hay un error, mostrar el formulario de login
    return render(request, 'login.html')


@csrf_protect
def registrar_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        # Verifica si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return redirect('registrar')

        # Verifica si el correo electrónico ya existe
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está en uso.")
            return redirect('registrar')

        # Verifica que las contraseñas coincidan
        if password != password_confirmation:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('registrar')

        # Crear un nuevo usuario
        nuevo_usuario = User.objects.create_user(username=username, email=email, password=password)
        nuevo_usuario.save()
        messages.success(request, "Usuario registrado exitosamente.")
        return redirect('login')  # Redirige a la página de inicio de sesión

    return render(request, 'register.html')
@csrf_protect
def recuperar_views(request):
    """Vista para recuperar contraseña"""
    template_name = "recuperar.html"
    
    if request.method == 'POST':
        # Aquí puedes agregar la lógica para recuperar contraseña
        # Por ejemplo, enviar un correo electrónico para restablecer la contraseña
        pass
        
    return render(request, template_name)

def salir_view(request):
    """Vista para cerrar sesión"""
    logout(request)  # Llama a la función logout para cerrar la sesión del usuario
    messages.success(request, "Has cerrado sesión exitosamente")  # Mensaje de éxito
    return redirect('login')

@login_required
def home_view(request):
    """Vista para la página de inicio"""
    return render(request, 'index.html')
