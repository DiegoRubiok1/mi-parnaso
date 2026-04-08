# Mi Parnaso - Blog Literario

Plataforma de divulgación literaria desarrollada con Django, SQLite y Bootstrap.

## Funcionalidades:
- Publicación de artículos en la sección de _blog_ por parte de la redactora Carmen Huélamo en formato _markdown_.
- Gestion de usuarios.
- Foro de discusión
- Comentarios en los artículos del blog.
- Monitorización de datos de tráfico y usuarios.

## Tecnologías Utilizadas:
- **Backend**: Django
- **Base de Datos**: SQLite
- **Frontend**: HTMX, Bootstrap, CSS, JavaScript (en ese orden de relevancia)
- **Deploy**: Docker y Ubuntu Server 25.10

## Puesta en marcha (Ubuntu + Docker)

Pasos para desplegar la aplicación en un servidor debian utilizando Docker:

1. **Clonar el repositorio:**
   ```bash
   git clone git@github.com:DiegoRubiok1/mi-parnaso.git
   cd mi-parnaso
   ```

2. **Preparar la base de datos y archivos:**
   Es necesario crear el archivo de la base de datos SQLite en el host para que Docker lo monte correctamente como un 
   archivo (y no como un directorio):
   ```bash
   touch db.sqlite3
   ```

3. **Configurar el entorno:**
   Crear un archivo `.env.prod` basándose en la configuración de Django (necesario para el contenedor de la web):
   ```bash
   nvim .env.prod
   ```
   *(Asegurarse de configurar `DEBUG=False`, `ALLOWED_HOSTS`, y una `SECRET_KEY` segura).*

4. **Desplegar con Docker Compose:**
   ```bash
   docker compose up -d --build
   ```

5. **Ejecutar migraciones y crear superusuario:**
   Una vez que el contenedor esté en marcha, prepara la base de datos:
   ```bash
   docker compose exec web python manage.py migrate
   docker compose exec web python manage.py createsuperuser
   ```

## Licencia

Este proyecto está bajo la **Licencia MIT** para su código fuente. Sin embargo, todos los **artículos del blog y 
contenidos literarios** son propiedad intelectual exclusiva de Carmen Huélamo y no están incluidos bajo esta licencia de 
código abierto. Consulta el archivo [LICENSE](LICENSE) para más detalles.
