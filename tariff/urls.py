from django.urls import path

from .views import index, tariff_detail, delete_tariff, tariff_create

app_name = 'tariff'

urlpatterns = [
    path('', index, name='index'),
    path('tariff/<int:pk>/', tariff_detail, name="tariff-detail"),
    path('delete/<int:pk>/', delete_tariff, name='delete'),
    path('tariff/create/', tariff_create, name='create'),
]