from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


def novo_usuario(request):
    # Tipo, validar, informar e salvar
    # Tipo
    if request.method == 'POST':
        fomulario = UserRegisterForm(request.POST)
        # Validar
        if fomulario.is_valid():
            # Salvar
            fomulario.save()
            # Informar
            usuario = fomulario.cleaned_data.get('username')
            messages.success(request, f'O usuário {
                             usuario} foi criado com sucesso!')

            return redirect('login')
    else:
        fomulario = UserRegisterForm()

    return render(request, 'usuarios/registrar.html', {'formulario': fomulario})
