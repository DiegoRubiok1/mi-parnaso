# Requisitos del blog literario (versión cerrada)

## 1) Objetivo
Sustituir el blog estático actual (Hugo + Nginx) por una plataforma dinámica para divulgación literaria,
con gestión de artículos en Markdown, comentarios, foro y administración centralizada.

## 2) Alcance MVP (primera entrega)

Incluye:
- Registro, login, logout y perfil básico de usuario.
- Publicación y gestión de artículos desde panel de administración.
- Conversión de Markdown a HTML seguro.
- Comentarios en artículos para usuarios autenticados.
- Foro básico (temas + respuestas) con advertencia de contenido sensible.
- Baneo de usuarios para impedir su participación en el foro.
- Estadística básica de visitas por artículo.

No incluye en MVP:
- Notificaciones por email.
- Reacciones, likes o sistema de reputación.
- Búsqueda avanzada o recomendador.
- Moderación avanzada (reportes, colas, auditoría detallada).

## 3) Decisiones técnicas recomendadas

- Backend: `Django` (Python).
- Base de datos: `SQLite3`.
- Frontend: `Django Templates + HTMX + Bootstrap`.
- Despliegue: contenedor `Docker` en servidor Ubuntu.

Rationale (enfoque principiante):
- Evita la complejidad de una SPA (React/Vue) para el primer proyecto.
- Mantiene la lógica en servidor y minimiza JavaScript manual.
- Permite añadir interactividad progresiva con HTMX.

## 4) Requisitos funcionales

### 4.1 Usuarios y autenticación
- RF-USER-01: El sistema permite registro con `username` único, `email` único y contraseña.
- RF-USER-02: El sistema permite login y logout.
- RF-USER-03: Cada usuario puede editar su perfil con foto y biografía.
- RF-USER-04: El sistema impide registro con email duplicado.
- RF-USER-05: Usuario baneado no puede crear temas ni responder en foro.

### 4.2 Panel de administración
- RF-ADMIN-01: Existe acceso al panel para personal administrador.
- RF-ADMIN-02: El administrador puede crear artículos con título, contenido Markdown (con imágenes), imagen destacada y 
               etiquetas.
- RF-ADMIN-03: El administrador puede previsualizar el artículo antes de publicar.
- RF-ADMIN-04: El administrador puede editar y eliminar artículos.
- RF-ADMIN-05: El administrador puede ver contador de visitas por artículo.
- RF-ADMIN-06: El administrador puede banear/desbanear usuarios.

Nota de implementación:
- Se utilizará `Django Admin` como panel base.
- El superusuario inicial se crea desde variables de entorno del `.env` durante el bootstrap.

### 4.3 Blog principal
- RF-BLOG-01: La home lista artículos publicados con título, imagen destacada, fecha y autor.
- RF-BLOG-02: La vista de detalle muestra contenido renderizado desde Markdown.
- RF-BLOG-03: Solo usuarios autenticados pueden comentar artículos.
- RF-BLOG-04: Cada comentario muestra autor, fecha y contenido.

### 4.4 Foro
- RF-FORUM-01: Solo usuarios autenticados pueden crear temas.
- RF-FORUM-02: Solo usuarios autenticados pueden responder temas.
- RF-FORUM-03: Antes de acceder al foro se muestra advertencia de contenido sensible y normas básicas.
- RF-FORUM-04: Usuarios baneados no pueden publicar en foro.

### 4.5 Markdown y seguridad de contenido
- RF-MD-01: El contenido de artículos se escribe en Markdown.
- RF-MD-02: El sistema convierte Markdown a HTML al mostrar/publicar.
- RF-MD-03: El HTML resultante se sanitiza para evitar XSS.

### 4.6 Estadísticas
- RF-STATS-01: Cada vista de artículo incrementa contador de visitas.
- RF-STATS-02: El administrador puede consultar visitas totales por artículo en el panel.

## 5) Criterios de aceptación (verificables)

### 5.1 Registro y autenticación
- CA-01: Dado un email existente, cuando intento registrarme con ese email, entonces el sistema rechaza el registro.
- CA-02: Dado un usuario válido, cuando inicia sesión, entonces accede a su sesión autenticada.
- CA-03: Dado un usuario autenticado, cuando cierra sesión, entonces la sesión queda invalidada.

### 5.2 Administración de artículos
- CA-04: Dado un administrador, cuando crea un artículo con título y contenido, entonces el artículo queda publicado.
- CA-05: Dado un artículo existente, cuando el administrador lo edita, entonces los cambios se reflejan en la vista 
  pública.
- CA-06: Dado un artículo, cuando se previsualiza, entonces se muestra HTML renderizado desde Markdown antes de 
  publicar.

### 5.3 Comentarios
- CA-07: Dado un usuario no autenticado, cuando intenta comentar, entonces el sistema exige login.
- CA-08: Dado un usuario autenticado, cuando publica comentario, entonces este aparece con autor y fecha.

### 5.4 Foro y baneo
- CA-09: Dado un usuario autenticado no baneado, cuando crea tema en foro, entonces el tema se publica.
- CA-10: Dado un usuario baneado, cuando intenta crear tema o responder, entonces el sistema bloquea la acción.
- CA-11: Dado cualquier usuario, cuando entra al foro por primera vez en sesión, entonces ve el aviso de contenido sensible.

### 5.5 Estadísticas
- CA-12: Dado un artículo, cuando se abre su detalle, entonces su contador de visitas aumenta en +1.
- CA-13: Dado un administrador en panel, cuando consulta artículos, entonces puede ver visitas acumuladas por artículo.

## 6) Requisitos no funcionales

- RNF-01: Interfaz responsive (móvil, tableta y escritorio).
- RNF-02: Persistencia en `SQLite3`.
- RNF-03: Backend en `Django`.
- RNF-04: Despliegue self-hosted con `Docker` en Ubuntu Server.
- RNF-05: Validación de formularios en backend.
- RNF-06: Protección CSRF activa en formularios.
- RNF-07: Sanitización de HTML renderizado desde Markdown.

## 7) Roadmap por fases

### Fase 1 - MVP funcional
- Usuarios: registro/login/logout/perfil.
- Blog: listado + detalle + comentarios autenticados.
- Admin: CRUD de artículos + previsualización Markdown.
- Foro: temas/respuestas + aviso sensible.
- Baneo básico y contador de visitas.

### Fase 2 - Endurecimiento
- Tests de autenticación, permisos y flujos críticos.
- Mejoras de UX (paginación y feedback de formularios).
- Métricas diarias de visitas por artículo.

### Fase 3 - Post-MVP
- Moderación avanzada (reportes, ocultación de contenido).
- Búsqueda y filtros por etiquetas.
- Integraciones opcionales (email de confirmación, analítica externa).

## 8) Backlog post-MVP (priorizado)

- BL-01: Verificación de email por enlace.
- BL-02: Recuperación de contraseña por correo.
- BL-03: Búsqueda de artículos y foro.
- BL-04: Filtros por etiquetas y autor.
- BL-05: Sistema de reportes y moderación avanzada.
- BL-06: Dashboard de analítica con series temporales.

## 9) Dudas cerradas para esta versión

Para evitar bloqueo en implementación, se fijan estas decisiones:
- Validación de email en MVP = unicidad de email (sin confirmación por enlace).
- Estadísticas en MVP = contador total por artículo.
- Baneo en MVP = bloqueo de escritura en foro (crear tema/responder).
- Panel admin en MVP = `Django Admin`, no panel custom.
