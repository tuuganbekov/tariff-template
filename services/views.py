from django.shortcuts import render, redirect

from .models import Services
from .forms import ServiceForm, ServiceModelForm

def service_list(request):
    services = Services.objects.all()
    return render(request, 'services/service-list.html', locals())


def service_detail(request, pk):
    service = Services.objects.get(id=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            print("cleaned data: ", form.cleaned_data)
            service.title = form.cleaned_data["title"]
            service.description = form.cleaned_data["description"]
            service.price = form.cleaned_data["price"]
            service.image = form.cleaned_data["image"]
            service.save()
        return redirect("tariff:index")
    else:
        form = ServiceForm(
            initial={
                "title": service.title,
                "description": service.description,
                "price": service.price
            }
        )
    return render(request, 'services/service-detail.html', locals())


def delete_service(request, pk):
    service = Services.objects.get(id=pk)
    if request.method == "POST":
        service.delete()
        return redirect("services:service-list")
    

def create_service(request):
    if request.method == "POST":
        form = ServiceModelForm(request.POST, request.FILES)
        if form.is_valid():
            service = Services.objects.create(
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                price = form.cleaned_data["price"],
                image = form.cleaned_data["image"],
            )
            return redirect("services:service-list")
    else:
        form = ServiceModelForm()
        return render(request, "services/service-create.html", locals())
