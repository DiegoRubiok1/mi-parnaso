# MVP Carmina - Blog Literario

Plataforma de divulgación literaria desarrollada con Django, SQLite y Bootstrap.

## Arranque rápido

### Opción 1: Script automático
```bash
chmod +x bootstrap.sh
./bootstrap.sh
python manage.py runserver
```

### Opción 2: Manual
```bash
# Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate  # o en Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

Accede a:
- **Home**: http://localhost:8000
- **Admin**: http://localhost:8000/admin
- **Blog**: http://localhost:8000/blog/
- **Foro**: http://localhost:8000/forum/

## 📋 Estructura del proyecto

```
carmina_web/
├── config/                  # Configuración Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── core/               # Home y utilidades
│   ├── accounts/           # Usuarios, perfiles, autenticación
│   ├── blog/               # Artículos, comentarios
│   └── forum/              # Temas y respuestas
├── templates/              # Templates HTML
├── static/                 # CSS, JS, imágenes
├── media/                  # Subidas de usuarios
├── manage.py
├── requirements.txt
└── .env                    # Configuración local
```

## ✅ Funcionalidades implementadas (MVP)

### Autenticación (Semana 2)
- [x] Registro de usuarios
- [x] Login/Logout
- [x] Perfil editable (foto + biografía)
- [x] Validación de email único
- [x] Señal para auto-crear Profile

### Blog (Semana 3-4)
- [x] Modelos Post, Tag, PostComment
- [x] Listado de artículos publicados
- [x] Vista detalle con contador de visitas
- [x] Comentarios (solo autenticados)
- [x] Draft/Published states

### Foro (Semana 5)
- [x] Modelos ForumThread, ForumReply
- [x] Crear temas y respuestas
- [x] Bloqueo de usuarios baneados
- [x] Aviso de contenido sensible

### Admin
- [x] Gestión de usuarios (incluye baneo)
- [x] CRUD de artículos y etiquetas
- [x] Gestión de comentarios
- [x] Gestión de temas y respuestas
- [x] Estadísticas de visitas por artículo

## 🧪 Tests

Ejecutar todos los tests:
```bash
python manage.py test apps.accounts.tests apps.blog.tests apps.forum.tests -v 2
```

Cobertura:
- Registro con email duplicado
- Creación automática de perfil
- Visibilidad de posts publicados
- Incremento de contador de visitas
- Bloqueo de comentarios no autenticados
- Bloqueo de foro para baneados

## 📝 Próximos pasos (Semana 6+)

### Endurecimiento (Semana 6)
- [ ] Tests adicionales para permisos
- [ ] Validación frontend y backend mejorada
- [ ] Mensajes de error más claros
- [ ] Responsive design refinado

### Post-MVP (Backlog)
- [ ] Sanitización Markdown HTML
- [ ] Preview de artículos con HTMX
- [ ] Búsqueda y filtros por etiquetas
- [ ] Verificación de email por enlace
- [ ] Recuperación de contraseña
- [ ] Sistema de reportes moderados

## 🛠 Stack técnico

- **Backend**: Django 5.2.1
- **BD**: SQLite3
- **Frontend**: Django Templates + Bootstrap 5 + HTMX
- **Imágenes**: Pillow
- **Markdown**: markdown (preparado para Semana 4)
- **Sanitización**: bleach (preparado para Semana 4)

## 📚 Requisitos completos

Ver `docs/requirements.md` para especificación completa del proyecto.

## 🔧 Configuración (.env)

Ejemplo de `.env`:
```env
DEBUG=True
SECRET_KEY=tu-clave-secreta-aqui
ALLOWED_HOSTS=127.0.0.1,localhost

DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin123
```

## 📄 Licencia

Este proyecto es de código abierto para fines educativos.

