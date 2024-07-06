# Import apps
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from payment.autentication import paypalToken
from payment import repository
from .models import Payment
from rest_framework import generics
from .serializers import PaymentSerializer
from rest_framework import status

# Update in the platform

class PaymentOrderCreate(APIView):
    name = 'payment-service'

    def post(self, request, pk, token, format=None):
        order = repository.get_order(pk=pk, token=token)
        print(f'Order payment: {order} ')
        if order.status_code == 200:
            response = repository.paypal_payment(request=request)
            if response.status_code == 201:
                repository.get_order(pk=pk, token=token, data={
                    'paidAt': datetime.now(),
                    'isPaid': True,
                })

                payment_data = {
                    'order': order.json()['id'],
                    'user': order.json()['user'],
                    'payment_status': True,
                    'currency': request.data['purchase_units'][0]['amount']['currency_code'],
                    'amount': request.data['purchase_units'][0]['amount']['value']
                }
                serializer = PaymentSerializer(data=payment_data)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'errors': 'order not found', 'status': order.status_code})


class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all() 
    serializer_class = PaymentSerializer
    name = 'payment-list'
