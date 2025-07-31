# Guía de Despliegue para Producción

## 🚀 Preparación para Producción

### 1. Configuración Inicial

Antes de desplegar, asegúrate de tener instalado:
- Python 3.8+
- Node.js 16+
- npm

### 2. Pasos para el Build de Producción

#### Opción A: Usando el script automatizado
```bash
# Desde el directorio raíz del proyecto
python build_production.py
```

#### Opción B: Pasos manuales
```bash
# 1. Navegar al directorio del tema
cd codeauni_vip/theme/static_src

# 2. Instalar dependencias de Node.js
npm install

# 3. Compilar CSS para producción
npm run build-prod

# 4. Volver al directorio del proyecto Django
cd ../../

# 5. Recolectar archivos estáticos
python manage.py collectstatic --noinput

# 6. Ejecutar migraciones
python manage.py migrate
```

### 3. Configuración del Servidor

#### Para desarrollo local:
```bash
python manage.py runserver
```

#### Para producción:
```bash
# Usar la configuración de producción
export DJANGO_SETTINGS_MODULE=config.settings_production
python manage.py runserver 0.0.0.0:8000
```

### 4. Configuración de Archivos Estáticos

#### Con Nginx (recomendado):
```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location /static/ {
        alias /ruta/a/tu/proyecto/staticfiles/;
    }

    location /media/ {
        alias /ruta/a/tu/proyecto/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### Con Apache:
```apache
<VirtualHost *:80>
    ServerName tu-dominio.com
    
    Alias /static/ /ruta/a/tu/proyecto/staticfiles/
    Alias /media/ /ruta/a/tu/proyecto/media/
    
    <Directory /ruta/a/tu/proyecto/staticfiles>
        Require all granted
    </Directory>
    
    <Directory /ruta/a/tu/proyecto/media>
        Require all granted
    </Directory>
</VirtualHost>
```

### 5. Variables de Entorno

Crea un archivo `.env` en el directorio raíz:
```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com
```

### 6. Verificación

Después del despliegue, verifica que:
- ✅ Los estilos CSS se cargan correctamente
- ✅ Las imágenes se muestran
- ✅ Los archivos estáticos se sirven desde `/static/`
- ✅ Los archivos de media se sirven desde `/media/`

### 7. Solución de Problemas

#### Si los estilos no se cargan:
1. Verifica que el archivo `styles.css` existe en `theme/static/css/`
2. Ejecuta `npm run build-prod` en `theme/static_src/`
3. Ejecuta `python manage.py collectstatic --noinput`
4. Verifica que `STATIC_ROOT` está configurado correctamente

#### Si hay errores 404:
1. Verifica que `ALLOWED_HOSTS` incluye tu dominio
2. Asegúrate de que `DEBUG = False` en producción
3. Verifica la configuración del servidor web

### 8. Comandos Útiles

```bash
# Verificar archivos estáticos
python manage.py collectstatic --dry-run

# Limpiar archivos estáticos
python manage.py collectstatic --clear --noinput

# Verificar configuración
python manage.py check --deploy

# Crear superusuario
python manage.py createsuperuser
```

## 📝 Notas Importantes

- **Nunca** uses `DEBUG = True` en producción
- **Siempre** usa HTTPS en producción
- **Configura** un servidor web (Nginx/Apache) para servir archivos estáticos
- **Mantén** actualizadas las dependencias
- **Haz** backups regulares de la base de datos 