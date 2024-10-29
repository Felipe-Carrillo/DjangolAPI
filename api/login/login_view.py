from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_view(request):
    """Vista para el inicio de sesión"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña inválidos')
    
    return render(request, 'login.html')

@csrf_protect
def registrar_views(request):
    """Vista para el registro de usuarios"""
    template_name = "register.html"
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        # Verificar si las contraseñas coinciden
        if password != password_confirmation:
            messages.error(request, "Las contraseñas no coinciden")
            return render(request, template_name)

        # Verificar si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return render(request, template_name)

        # Verificar si el correo ya existe
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya existe")
            return render(request, template_name)

        try:
            # Crear nuevo usuario
            user = User(
                username=username,
                email=email,
            )
            user.set_password(password)  # Configura la contraseña de forma segura
            user.is_active = True  # Cambiado a True para permitir el inicio de sesión
            user.save()

            # Mensaje de éxito y redirección al login
            messages.success(request, "Cuenta creada exitosamente. Puedes iniciar sesión ahora.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error al crear la cuenta: {str(e)}")
            return render(request, template_name)

    # Retornar la plantilla en caso de GET
    return render(request, template_name)

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
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente")
    return redirect('login')

@login_required
def home_view(request):
    """Vista para la página de inicio"""
    return render(request, 'index.html')