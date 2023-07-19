from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('order/<int:pk>', views.order, name='order'),
    path('order_delete/<int:pk>', views.delete, name='order_delete')
]