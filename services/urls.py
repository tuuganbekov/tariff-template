from django.urls import path

from .views import service_detail, service_list

app_name = 'services'

urlpatterns = [
    path('services/', service_list, name='service-list'),
    path('services/<int:pk>/', service_detail, name='service-detail'),
]
