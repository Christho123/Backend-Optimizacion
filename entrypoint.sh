#!/bin/bash

# Script de entrada para Docker
set -e

# Función para esperar a que la base de datos esté lista
wait_for_db() {
    echo "Esperando a que la base de datos esté lista..."
    while ! python manage.py check --database default 2>&1; do
        echo "Base de datos no disponible, esperando..."
        sleep 2
    done
    echo "Base de datos lista!"
}

# Función para esperar a que Redis esté listo
wait_for_redis() {
    echo "Esperando a que Redis esté listo..."
    while ! python -c "import redis; redis.Redis.from_url('$REDIS_URL').ping()" 2>/dev/null; do
        echo "Redis no disponible, esperando..."
        sleep 2
    done
    echo "Redis listo!"
}

# Crear directorios necesarios
mkdir -p /app/staticfiles /app/media /app/logs

# Esperar a que los servicios estén listos
wait_for_db
wait_for_redis

# Ejecutar migraciones (comentado para usar BD local)
# echo "Ejecutando migraciones..."
# python manage.py migrate --noinput

# Recolectar archivos estáticos (se ejecuta desde docker-compose en 'web')
# echo "Recolectando archivos estáticos..."
# python manage.py collectstatic --noinput

# Crear superusuario si no existe (comentado para usar BD local)
# echo "Verificando superusuario..."
# python manage.py shell -c "
# from django.contrib.auth import get_user_model
# User = get_user_model()
# if not User.objects.filter(is_superuser=True).exists():
#     try:
#         User.objects.create_superuser(username='admin', email='admin@example.com', password='admin123')
#         print('Superusuario creado: admin/admin123')
#     except Exception as e:
#         print(f'Error creando superusuario: {e}')
# else:
#     print('Superusuario ya existe')
# "

# Ejecutar el comando principal
echo "Iniciando aplicación..."
exec "$@"
