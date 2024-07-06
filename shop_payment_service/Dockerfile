FROM python:3.9.5

ENV PYTHONUNBUFFERED 1

WORKDIR /shop_payment_service

COPY shop_payment_service/requirements.txt /shop_payment_service/requirements.txt

RUN pip install -r requirements.txt

COPY shop_payment_service /shop_payment_service

# # Create and apply migrations during the Docker image build process
RUN python3 shop_payment_service/manage.py makemigrations payment
RUN python3 shop_payment_service/manage.py migrate payment

# FROM django_microservices
# WORKDIR /shop_payment_service
# COPY . /shop_payment_service
