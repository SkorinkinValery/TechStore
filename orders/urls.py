#Создание заказа
from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('add/', views.order_add, name='add'),
    path('update/', views.order_update_status, name='update'),
]