# # Use the official Python 3.9.5 image as the parent image
FROM python:3.9.5

ENV PYTHONUNBUFFERED 1

WORKDIR /shop_product_service

COPY shop_product_service/requirements.txt /shop_product_service/requirements.txt

RUN pip install -r requirements.txt

COPY shop_product_service /shop_product_service

# # Create and apply migrations during the Docker image build process
RUN python3 shop_product_service/manage.py makemigrations shop
RUN python3 shop_product_service/manage.py migrate shop


# FROM django_microservices
# WORKDIR /shop_product_service
# COPY . /shop_product_service