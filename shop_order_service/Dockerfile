FROM python:3.9.5

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY shop_order_service/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY shop_order_service /app/
