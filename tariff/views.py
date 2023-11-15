from django.shortcuts import render, redirect

# Create your views here.
from .forms import TariffForm
from .models import Tariff


def index(request):
    tariffs = Tariff.objects.all()
    return render(request, 'tariff/tariff-list.html', locals())


def tariff_detail(request, pk):
    tariff = Tariff.objects.get(id=pk)
    return render(request, 'tariff/tariff-detail.html', locals())