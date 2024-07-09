# # Use the official Python 3.9.5 image as the parent image
FROM python:3.9.5

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY shop_product_service/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY shop_product_service/ /app/
