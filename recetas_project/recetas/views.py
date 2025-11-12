from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Receta
from .forms import ContactoForm
from django.contrib import messages
from django.shortcuts import redirect

def inicio(request):
    recetas_recientes = Receta.objects.all()[:6]
    return render(request, 'inicio.html', {'recetas_recientes': recetas_recientes})

class RecetasListView(ListView):
    model = Receta
    template_name = 'recetas_lista.html'
    context_object_name = 'recetas'
    paginate_by = 9

class RecetaDetailView(DetailView):
    model = Receta
    template_name = 'receta_detalle.html'
    context_object_name = 'receta'

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            messages.success(request, "Mensaje enviado con éxito.")
            return redirect('confirmacion')
        else:
            messages.warning(request, "Por favor, completa todos los campos correctamente.")
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})

def confirmacion(request):
    return render(request, 'confirmacion.html')

def error_404(request, exception):
    return render(request, 'error_404.html', status=404)
