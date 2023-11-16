from django.urls import path

from .views import service_detail, service_list, delete_service, create_service

app_name = 'services'

urlpatterns = [
    path('services/', service_list, name='service-list'),
    path('services/<int:pk>/', service_detail, name='service-detail'),
    path('services/delete/<int:pk>/', delete_service, name='delete-service'),
    path('services/create/', create_service, name='create-service'),
]
