#!/bin/bash
# Script de bootstrap para levantar el proyecto Django en local

set -e

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Carmina Blog - Bootstrap Local ===${NC}"

# 1. Virtual environment
if [ ! -d ".venv" ]; then
    echo -e "${BLUE}Creando virtual environment...${NC}"
    python3 -m venv .venv
fi

echo -e "${BLUE}Activando virtual environment...${NC}"
source .venv/bin/activate

# 2. Instalar dependencias
echo -e "${BLUE}Instalando dependencias...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

# 3. Migraciones
echo -e "${BLUE}Aplicando migraciones...${NC}"
python manage.py migrate

# 4. Crear superusuario (solo si no existe)
echo -e "${BLUE}Verificando superusuario...${NC}"
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    print("Creando superusuario admin...")
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superusuario creado. Usa: admin / admin123")
else:
    print("Superusuario ya existe.")
END

# 5. Crear directorios necesarios
mkdir -p static media logs

echo -e "${GREEN}✓ Setup completado!${NC}"
echo -e "${GREEN}✓ Para iniciar el servidor: python manage.py runserver${NC}"
echo -e "${GREEN}✓ Admin: http://localhost:8000/admin${NC}"
echo -e "${GREEN}✓ Home: http://localhost:8000${NC}"

