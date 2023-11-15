from django.urls import path

from .views import index, tariff_detail

app_name = 'tariff'

urlpatterns = [
    path('', index, name='index'),
    path('tariff/<int:pk>/', tariff_detail, name="tariff-detail")
]