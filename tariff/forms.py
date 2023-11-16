from django import forms

from .models import Tariff


class TariffForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control"}
        ),
        required=True
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control"}
        )
    )
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={"class": "form-control"}
        ),
        required=True
    )

class TariffModelForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }
