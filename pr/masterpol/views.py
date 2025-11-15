from django.shortcuts import render, redirect, get_object_or_404
from .models import Partner, TypeProduct, TypeMaterial, Postavki
from .forms import PartnerForm
import math


def partner_list(request):
    partners = Partner.objects.all()
    #postavki = Postavki.objects.all()
    return render(request, 'partner_list.html', {'partners': partners})


def partner_add(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm()
    return render(request, 'partner_form.html', {'form': form})


def partner_edit(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'partner_form.html', {'form': form})


def partner_history(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    postavki = Postavki.objects.filter(partner=partner)
    #discount = partner.discount(postavki)

    return render(request, "partner_history.html", {
        "partner": partner,
        "postavki": postavki
    })


def calculate_material(type_product_id, type_material_id, count, p1, p2):
    try:
        if count <= 0 or p1 <= 0 or p2 <= 0:
            return -1

        type_product = TypeProduct.objects.filter(id=type_product_id).first()
        type_material = TypeMaterial.objects.filter(id=type_material_id).first()

        if not type_product or not type_material:
            return -1

        k = float(type_product.kef)

        waste = float(type_material.waste_percent)

        material_per_one = p1 * p2 * k

        total_material = material_per_one * count

        total_with_waste = total_material * (1 + waste / 100)

        return math.ceil(total_with_waste)

    except Exception:
        return -1

    return render(request, "partner_history.html", {
        "partner": partner,
        "postavki": postavki,
        "discount": discount,
        "form": form,
        "result": result,
    })
