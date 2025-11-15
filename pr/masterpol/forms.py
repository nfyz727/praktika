from django import forms
from .models import Partner, TypeProduct, TypeMaterial


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['type', 'name', 'director', 'email', 'phone_number', 'address', 'inn', 'rate']

        widgets = {
            'type': forms.Select(),
            'director': forms.Select(),
            'address': forms.Select(),
        }


class MaterialCalcForm(forms.Form):
    type_product = forms.ModelChoiceField(
        queryset=TypeProduct.objects.all(),
        label="Тип продукции"
    )
    type_material = forms.ModelChoiceField(
        queryset=TypeMaterial.objects.all(),
        label="Тип материала"
    )
    count = forms.IntegerField(
        min_value=1,
        label="Количество получаемой продукции"
    )
    p1 = forms.FloatField(
        min_value=0.0001,
        label="Параметр 1"
    )
    p2 = forms.FloatField(
        min_value=0.0001,
        label="Параметр 2"
    )