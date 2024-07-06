#!/bin/bash

cd /usercode/services

# Define variáveis de ambiente necessárias para a execução do Docker
export USER=$(whoami)
export HOME=/home/$USER

docker-compose up -d




 