# Plan de implementacion MVP (Django + SQLite)

Este documento aterriza `docs/requirements.md` en una estructura técnica ejecutable para el MVP.

## 1) Estructura propuesta de proyecto y apps

```text
carmina_web/
  manage.py
  config/
    settings.py
    urls.py
    wsgi.py
    asgi.py
  apps/
    core/
    accounts/
    blog/
    forum/
```

### Responsabilidades por app

- `core`
  - Layout base, home publica, paginas estaticas (terminos, aviso foro)
  - utilidades compartidas (sanitizacion markdown, helpers)
- `accounts`
  - usuario, perfil, registro/login/logout, permisos, baneo
  - formularios y vistas de perfil
- `blog`
  - articulos, etiquetas, comentarios, contador de visitas
  - vistas de listado/detalle, endpoints HTMX (preview markdown)
- `forum`
  - temas y respuestas
  - validacion de usuario baneado antes de publicar

### Namespaces de URL

- `core:*` -> `/`
- `accounts:*` -> `/accounts/`
- `blog:*` -> `/blog/`
- `forum:*` -> `/forum/`
- `admin` -> `/admin/`

## 2) Modelos base (diseno)

## `accounts`

- `User` (recomendado custom desde inicio)
  - `username` (unique)
  - `email` (unique, index)
  - `is_active`
  - `is_staff`
  - `is_banned` (bool, default=False)
  - `date_joined`

- `Profile`
  - `user` (OneToOne -> User)
  - `photo` (ImageField, opcional)
  - `bio` (TextField, max sugerido 500)

- `BanLog` (opcional MVP+, pero util)
  - `user` (FK -> User)
  - `reason` (TextField)
  - `created_by` (FK -> User admin)
  - `created_at`

## `blog`

- `Tag`
  - `name` (unique)
  - `slug` (unique)

- `Post`
  - `title`
  - `slug` (unique)
  - `author` (FK -> User)
  - `content_md` (TextField)
  - `content_html` (TextField, sanitizado)
  - `featured_image` (ImageField, opcional)
  - `status` (draft/published)
  - `published_at` (nullable)
  - `view_count` (PositiveInteger, default=0)
  - `created_at`, `updated_at`
  - `tags` (M2M -> Tag)

- `PostComment`
  - `post` (FK -> Post)
  - `author` (FK -> User)
  - `content` (TextField)
  - `created_at`

## `forum`

- `ForumThread`
  - `title`
  - `slug` (unique)
  - `author` (FK -> User)
  - `content`
  - `created_at`, `updated_at`
  - `is_locked` (bool, default=False)

- `ForumReply`
  - `thread` (FK -> ForumThread)
  - `author` (FK -> User)
  - `content`
  - `created_at`

## 3) Orden tecnico recomendado

1. **Bootstrap**: proyecto, settings, apps, templates base, static/media, `.env`.
2. **Autenticacion**: user custom + login/logout/registro + perfil.
3. **Admin**: registrar modelos y acciones de baneo/desbaneo.
4. **Blog**: modelos `Post/Tag/PostComment`, CRUD admin, listado/detalle publico.
5. **Markdown seguro**: pipeline markdown -> html sanitizado + preview HTMX.
6. **Comentarios**: solo autenticados en detalle de articulo.
7. **Foro**: `ForumThread/ForumReply` + aviso sensible + bloqueo por baneo.
8. **Estadísticas**: `view_count` por artículo en detalle y visibilidad en admin.
9. **Calidad**: tests mínimos de auth, permisos, baneo y comentarios.
10. **Deploy base**: Dockerfile + docker-compose (opcional en local), checklist Ubuntu.

## 4) Checklist semanal (6 semanas)

## Semana 1 - Base del proyecto

- [ ] Crear proyecto Django y carpeta `apps/`
- [ ] Configurar `.env` y lectura de variables
- [ ] Configurar templates, static y media
- [ ] Crear `User` custom y migraciones iniciales
- [ ] Crear layout base con Bootstrap

Entregable: app inicia correctamente, migraciones aplicadas, login de admin posible.

## Semana 2 - Accounts

- [ ] Registro, login, logout
- [ ] Perfil editable (foto + bio)
- [ ] Validar email unico en formulario
- [ ] Proteger rutas con `LoginRequiredMixin`
- [ ] Tests: registro duplicado, login/logout

Entregable: flujo completo de usuario y perfil.

## Semana 3 - Blog (publicacion)

- [ ] Modelos `Tag`, `Post`, `PostComment`
- [ ] Admin CRUD de articulos y etiquetas
- [ ] Home con listado de publicados
- [ ] Detalle de articulo
- [ ] Estado draft/published

Entregable: publicar y ver articulos en frontend.

## Semana 4 - Markdown, comentarios y stats

- [ ] Render Markdown -> HTML sanitizado
- [ ] Preview de Markdown via HTMX
- [ ] Comentarios solo autenticados
- [ ] Mostrar autor/fecha/contenido en comentarios
- [ ] Incrementar `view_count` al abrir detalle

Entregable: `CA-06`, `CA-07`, `CA-08`, `CA-12` cumplidos.

## Semana 5 - Foro y baneo

- [ ] Modelos `ForumThread` y `ForumReply`
- [ ] Vistas crear/listar/detalle/responder
- [ ] Aviso sensible antes de entrar al foro
- [ ] Bloqueo de creacion/respuesta para baneados
- [ ] Acciones admin banear/desbanear

Entregable: `CA-09`, `CA-10`, `CA-11` cumplidos.

## Semana 6 - Endurecimiento y despliegue base

- [ ] Tests de permisos y flujos criticos
- [ ] Ajustes UX responsive y mensajes de error
- [ ] Dockerfile + compose local
- [ ] Script bootstrap superusuario desde `.env`
- [ ] Checklist de despliegue Ubuntu

Entregable: MVP estable para pasar a post-MVP.

## 5) Comandos iniciales (bash, adaptables)

```bash
cd /home/drubioc/Code/web/carmina_web
python -m venv .venv
source .venv/bin/activate
pip install django python-dotenv markdown bleach pillow django-htmx
pip freeze > requirements.txt

# Crea proyecto en la raiz actual
python -m django startproject config .

# Crea apps
mkdir -p apps
python manage.py startapp core apps/core
python manage.py startapp accounts apps/accounts
python manage.py startapp blog apps/blog
python manage.py startapp forum apps/forum

# Migraciones iniciales
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Nota: los comandos de apps pueden variar según tu estructura de `INSTALLED_APPS` y `AppConfig.name`.

