# 🎨 Sistema de estilos neoclásicos - Carmina

## Descripción

Los estilos de Carmina siguen una **estética neoclásica elegante** con:
- **Tipografía**: Times New Roman (serif) para un aspecto clásico
- **Paleta**: Colores tierra, dorados y grises
- **Diseño**: Minimalista, espacios limpios, bordes sutiles
- **Animaciones**: Transiciones suaves y elegantes

---

## 📁 Estructura

```
static/
└── css/
    └── style.css      # Estilos centralizados (todos los estilos)
```

El archivo `style.css` contiene:
- Variables CSS personalizadas (colores, tipografía, espaciado)
- Estilos base para todo el proyecto
- Componentes (navbar, botones, cards, formularios, etc.)
- Estilos responsivos para móvil

---

## 🎨 Paleta de colores

### Colores principales

| Nombre | Color | Código | Uso |
|--------|-------|--------|-----|
| Primary | Marrón tierra | `#8B7355` | Botones, links, bordes |
| Primary Light | Marrón claro | `#A0826D` | Hover state |
| Primary Dark | Marrón oscuro | `#6B5344` | Headings, text |
| Accent | Dorado | `#D4AF37` | Énfasis, accents |
| Accent Light | Dorado claro | `#E8C850` | Hover dorado |
| Neutral | Gris oscuro | `#3D3D3D` | Botones secundarios |
| Neutral Light | Crema | `#F5F3F0` | Fondos, navbar, footer |
| Neutral Lighter | Blanco roto | `#FEFDFB` | Fondo principal |

### Colores de estado

| Estado | Color | Código |
|--------|-------|--------|
| Success | Verde oliva | `#6B8E23` |
| Danger | Rojo tierra | `#8B4513` |
| Info | Azul clásico | `#2196F3` |
| Warning | Naranja clásico | `#FF9800` |

---

## 📝 Tipografía

### Fuentes

- **Serif (principal)**: `Times New Roman, Times, serif`
  - Headings (h1-h6)
  - Body text
  - Labels
  
- **Sans-serif (secundaria)**: `Segoe UI, Tahoma, Geneva, Verdana, sans-serif`
  - Formularios
  - Badges
  - Algunos elementos UI

### Tamaños

| Elemento | Tamaño | Peso |
|----------|--------|------|
| h1 | 2.5rem | 400 (normal) |
| h2 | 2rem | 400 |
| h3 | 1.5rem | 400 |
| Cuerpo | 1rem (16px) | 400 |
| Small | 0.9rem | 400 |

### Características

- **Letter-spacing**: 0.3-1px para elegancia
- **Line-height**: 1.7 (body), 1.8-1.9 (contenido)
- **Font-weight**: 400 (normal) en todo, sin bold excesivo

---

## 🔧 Componentes y su estilo

### Navbar

```css
/* Fondo crema con borde dorado inferior */
background-color: #F5F3F0;
border-bottom: 2px solid #D4AF37;
```

- Logo en pequeña capital (font-variant: small-caps)
- Links con underline en hover
- Transiciones suaves

### Botones

```css
/* Primario: marrón tierra */
.btn-primary {
    background-color: #8B7355;
    border: 2px solid #8B7355;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Hover: más oscuro y levantado */
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(44, 44, 44, 0.12);
}
```

### Tarjetas (Cards)

```css
/* Border sutil, sombra elegante */
border: 1px solid #D4D0CC;
box-shadow: 0 1px 3px rgba(44, 44, 44, 0.08);
border-radius: 4px;

/* Hover: borde dorado, sombra mayor */
.card:hover {
    border-color: #D4AF37;
    transform: translateY(-4px);
    box-shadow: 0 4px 6px rgba(44, 44, 44, 0.12);
}
```

### Formularios

```css
/* Border sutil, focus en primary */
border: 1px solid #D4D0CC;
border-radius: 2px;

.form-control:focus {
    border-color: #8B7355;
    box-shadow: 0 0 0 3px rgba(139, 115, 85, 0.1);
}
```

### Comentarios

```css
/* Fondo crema con borde izquierdo marrón */
background-color: #F5F3F0;
border-left: 3px solid #8B7355;
padding: 1rem;
border-radius: 2px;
```

---

## 📐 Espaciado (variables)

```css
--spacing-xs: 0.25rem
--spacing-sm: 0.5rem
--spacing-md: 1rem
--spacing-lg: 1.5rem
--spacing-xl: 2rem
--spacing-2xl: 3rem
```

Se usa consistentemente para:
- Padding de componentes
- Margins entre elementos
- Gap en flexbox/grid

---

## 🌓 Sombras

```css
--shadow-sm: 0 1px 3px rgba(44, 44, 44, 0.08);      /* Sutil */
--shadow-md: 0 4px 6px rgba(44, 44, 44, 0.12);      /* Normal */
--shadow-lg: 0 10px 15px rgba(44, 44, 44, 0.15);    /* Fuerte */
```

- Usadas en cards, botones en hover, modales
- Todas con opacidad baja para elegancia

---

## 📱 Responsive

El CSS incluye breakpoints:
- `@media (max-width: 768px)` - Tablets
- `@media (max-width: 576px)` - Móviles

Cambios:
- Headings más pequeños
- Padding reducido
- Navbar simplificada
- Botones más pequeños

---

## ✨ Animaciones

### Fade In
```css
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
```

### Hover effects
- Botones: `translateY(-2px)` + sombra
- Links: color dorado + border-bottom
- Cards: `translateY(-4px)` + border dorado

---

## 🔄 Cómo personalizar

Para cambiar la paleta, edita las variables CSS en la parte superior de `style.css`:

```css
:root {
    --color-primary: #8B7355;      /* Cambia aquí */
    --color-accent: #D4AF37;        /* Y aquí */
    /* etc */
}
```

Todos los componentes usarán las nuevas variables automáticamente.

---

## 📖 Uso en templates

Los estilos se aplican automáticamente gracias a las clases Bootstrap y CSS:

```html
<!-- Botón -->
<button class="btn btn-primary">Enviar</button>

<!-- Card -->
<div class="card">
    <div class="card-body">
        <h5 class="card-title">Título</h5>
        <p class="card-text">Contenido</p>
    </div>
</div>

<!-- Formulario -->
<input type="text" class="form-control">

<!-- Comentario -->
<div class="comment">
    <div class="comment-header">
        <span class="comment-author">Autor</span>
        <span class="comment-date">Fecha</span>
    </div>
    <p class="comment-content">Contenido</p>
</div>
```

---

## 🎯 Principios de diseño

1. **Elegancia sin ostentación**: Colores tierra, sin colores brillantes
2. **Tipografía clásica**: Times New Roman para autoridad y legibilidad
3. **Espacios limpios**: Márgenes generosos, bordes sutiles
4. **Transiciones suaves**: Todo tiene `transition: all 0.3s ease`
5. **Accesibilidad**: Contraste suficiente, tamaños legibles
6. **Minimalismo**: Solo lo necesario, nada más

---

## 🚀 Próximas mejoras

- [ ] Agregar dark mode si es necesario
- [ ] Fuentes locales (Google Fonts) para no depender de system fonts
- [ ] Más animaciones elegantes
- [ ] Temas opcionales (clásico, moderno, etc.)

---

**Última actualización**: 27 de marzo de 2026  
**Diseño**: Neoclásico elegante  
**Tipografía**: Times New Roman  
**Paleta**: Tierra y dorados

