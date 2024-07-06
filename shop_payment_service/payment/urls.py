
from django.urls import path
from payment import views

urlpatterns = [

    path(f'{views.PaymentOrderCreate.name}/<int:pk>/token=<str:token>', views.PaymentOrderCreate.as_view(), name=views.PaymentOrderCreate.name),

    path(f'{views.PaymentList.name}/', views.PaymentList.as_view(), name=views.PaymentList.name),


]