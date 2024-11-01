from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto, Vehiculo
from django.contrib import messages
from decimal import Decimal

def principal(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'appoim/principal.html', {'proyectos': proyectos})


def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    vehiculos = proyecto.vehiculos.all()

    if request.method == 'POST':
        vehiculo_id = request.POST.get('vehiculo_id')
        kilometros_usados = request.POST.get('kilometros', 0)
        precio_combustible = request.POST.get('precio_combustible', 0)

        # Validar y guardar datos
        if vehiculo_id and kilometros_usados and precio_combustible:
            vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
            vehiculo.kilometros_usados += int(kilometros_usados)  # Actualiza los kilómetros
            vehiculo.precio_combustible = Decimal(precio_combustible)  # Actualiza el precio de combustible
            vehiculo.save()
            messages.success(request, 'Gastos guardados correctamente.')
            return redirect('detalle_proyecto', proyecto_id=proyecto_id)

    return render(request, 'appoim/detalle_proyecto.html', {'proyecto': proyecto, 'vehiculos': vehiculos})