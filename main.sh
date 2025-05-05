#!/bin/sh

# Mantener el dispositivo despierto permanentemente
termux-wake-lock

while true; do
    echo "Iniciando proceso de extracción..."

    # Actualizar los repositorios y asegurar que dos2unix está instalado
    pkg update -y
    pkg install -y dos2unix

    # Convertir el archivo de formato DOS a formato UNIX
    dos2unix /data/data/com.termux/files/home/Getnick/sacarCombinado.sh

    # Ejecutar el script combinado
    bash /data/data/com.termux/files/home/Getnick/sacarCombinado.sh

    # Ejecutar el script Python
    python /data/data/com.termux/files/home/Getnick/webhook.py

    echo "Proceso completado. Esperando 24 hrs para la siguiente ejecución..."

    # Esperar 5 minutos antes de la próxima ejecución
    sleep 86400
done