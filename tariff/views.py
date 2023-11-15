from django.shortcuts import render, redirect

# Create your views here.
from .forms import TariffForm
from .models import Tariff


def index(request):
    tariffs = Tariff.objects.all()
    return render(request, 'tariff/tariff-list.html', locals())


def tariff_detail(request, pk):
    tariff = Tariff.objects.get(id=pk)
    if request.method == "POST":
        form = TariffForm(request.POST, request.FILES)
        if form.is_valid():
            print("cleaned data: ", form.cleaned_data)
            tariff.title = form.cleaned_data["title"]
            tariff.description = form.cleaned_data["description"]
            tariff.price = form.cleaned_data["price"]
            tariff.image = form.cleaned_data["image"]
            tariff.save()
        return redirect("tariff:index")
    else:
        form = TariffForm(
            initial={
                "title": tariff.title,
                "description": tariff.description,
                "price": tariff.price
            }
        )
    return render(request, 'tariff/tariff-detail.html', locals())