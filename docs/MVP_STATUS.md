# Estado del MVP - Scaffold Django Completado

**Fecha**: 27 de marzo de 2026  
**Estado**: ✅ COMPLETADO - Scaffold base funcional  
**Próximas semanas**: Endurecimiento, markdown, y refinamientos

## 📊 Checklist de implementación

### Configuración base (Semana 1)
- [x] Proyecto Django creado en raíz con `config/`
- [x] Apps creadas: `core`, `accounts`, `blog`, `forum`
- [x] `settings.py` configurado con env loading, apps registradas, templates/media/static
- [x] URLs wired correctamente con namespaces por app
- [x] AppConfig corregidos a rutas completas (`apps.accounts`, etc.)
- [x] Template base con Bootstrap 5 y HTMX
- [x] Directorios `static/` y `media/` creados

### Autenticación (Semana 2)
- [x] Modelo `User` custom (AbstractUser)
- [x] Modelo `Profile` con foto y bio
- [x] Modelo `BanLog` para auditoría
- [x] Señal `post_save` que auto-crea Profile
- [x] FormularioS `RegisterForm` y `ProfileForm`
- [x] Vistas: `register_view`, `profile_view`
- [x] Admin: `CustomUserAdmin` con flag `is_banned` visible
- [x] URLs: register, login, logout, profile
- [x] Templates: register.html, login.html, profile.html
- [x] Tests: duplicado email, creación de profile

### Blog (Semana 3-4)
- [x] Modelos: `Tag`, `Post`, `PostComment`
- [x] Post con campos: title, slug, content_md, content_html, featured_image, status, published_at, view_count, tags
- [x] PostComment con autor, contenido, fecha
- [x] Vistas: `PostListView`, `PostDetailView`, `add_comment_view`
- [x] ListView muestra solo posts publicados
- [x] DetailView incrementa view_count correctamente
- [x] Comentarios solo para autenticados
- [x] Admin: `PostAdmin`, `TagAdmin`, `PostCommentAdmin` con filtros y búsqueda
- [x] URLs: listado, detalle, crear comentario
- [x] Templates: post_list.html, post_detail.html
- [x] Tests: posts publicados, incremento de visitas, login para comentar

### Foro (Semana 5)
- [x] Modelos: `ForumThread`, `ForumReply`
- [x] ForumThread con slug, is_locked, reply_count() method
- [x] ForumReply con contenido y fecha
- [x] Vistas: `ForumThreadListView`, `ForumThreadDetailView`, `create_thread_view`, `add_reply_view`
- [x] Bloqueo de usuarios baneados en `create_thread_view` y `add_reply_view`
- [x] Admin: `ForumThreadAdmin`, `ForumReplyAdmin`
- [x] URLs: listado, detalle, crear, responder
- [x] Templates: thread_list.html, thread_detail.html, create_thread.html (con aviso sensible)
- [x] Tests: baneado no puede crear/responder, autenticado sí puede

### Core (Inicio)
- [x] Vista `home_view` que lista últimos 5 posts publicados
- [x] Template home.html con Bootstrap layout
- [x] URL wiring en `core:home`
- [x] Navbar con links a todas las secciones

### Base de datos
- [x] Migraciones iniciales generadas sin errores
- [x] `python manage.py migrate` ejecutado correctamente
- [x] Tabla de usuarios custom, profiles, blog, foro creadas

### Tests
- [x] 8 tests implementados
- [x] Todos pasan (✅ OK - 8 tests en 2.99s)
- [x] Cobertura: auth, profiles, posts, visitas, comentarios, forum, baneo

### Documentación
- [x] `README.md` con instrucciones de arranque
- [x] `bootstrap.sh` para setup automático
- [x] `.env` con configuración de desarrollo
- [x] `requirements.txt` generado
- [x] `.gitignore` para Python/Django

### Servidor
- [x] `python manage.py runserver` levanta sin errores
- [x] StaticFiles warning por `static/` vacío (esperado)
- [x] Admin accesible en `/admin/` con credenciales admin/admin123
- [x] Todos los URLs del proyecto responden

## 📈 Métricas

| Métrica | Valor |
|---------|-------|
| Líneas de código Python | ~650 |
| Modelos creados | 9 |
| Vistas creadas | 10 |
| Templates creados | 11 |
| Tests implementados | 8 |
| Tests pasando | 8/8 (100%) |
| Migraciones | 4 |

## 🎯 Cumplimiento de criterios de aceptación (CA)

- [x] **CA-01**: Email duplicado rechazado ✓
- [x] **CA-02**: Login funciona ✓
- [x] **CA-03**: Logout funciona ✓
- [ ] **CA-04**: Admin puede crear artículos (sin markdown rendering aún)
- [ ] **CA-05**: Admin puede editar (no implementado aún)
- [ ] **CA-06**: Preview de markdown (Semana 4)
- [x] **CA-07**: Comentarios requieren login ✓
- [x] **CA-08**: Comentarios aparecen con autor/fecha ✓
- [x] **CA-09**: Usuario no baneado puede crear tema ✓
- [x] **CA-10**: Usuario baneado bloqueado ✓
- [x] **CA-11**: Aviso sensible en foro ✓
- [x] **CA-12**: Contador de visitas incrementa ✓
- [x] **CA-13**: Admin ve visitas en listado ✓

## 🚧 Pendiente (post-MVP)

- Markdown → HTML sanitizado (preparado: librerias instaladas)
- Preview con HTMX
- Edición/eliminación de artículos en admin UI
- Búsqueda de posts/temas
- Filtros por etiqueta
- Paginación refinada
- Tests de integración más completos
- Dockerización
- Deploy docs

## 🔗 Próximas semanas

### Semana 6 (Esta)
- Verificar todos los flujos en navegador
- Refinamientos UX (mensajes, validaciones)
- Tests adicionales de permisos
- Documentación para desarrolladores

### Semana 7+ (Post-MVP)
- Markdown rendering + sanitización
- Moderación avanzada
- Email notifications
- Metrics dashboard
- Docker + deploy

## ✨ Notas

- El proyecto está listo para desarrollo iterativo.
- Todos los modelos pueden ser extendidos sin breaking changes (debido a migraciones).
- Tests base permiten refactorización segura.
- Stack frontend (Templates + HTMX) es accesible para principiantes en JS.
- Base sólida para agregar funcionalidades semana a semana sin deuda técnica.

---

**Guardado en**: `/home/drubioc/Code/web/carmina_web/`  
**Siguiente**: Ver `README.md` e `implementation_plan.md` para más detalles.

