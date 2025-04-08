# 🦖 DinoScan AI: Aplicación Móvil de Clasificación de Dinosaurios con IA

## 📖 Descripción del Proyecto
DinoScan AI es una aplicación móvil que permite a los usuarios identificar especies de dinosaurios a partir de imágenes, utilizando modelos de Inteligencia Artificial. El sistema no solo realiza la clasificación, sino que también genera descripciones detalladas, hábitos y contexto histórico del espécimen, ofreciendo una experiencia educativa e interactiva.

Este repositorio contiene el código y recursos utilizados para el desarrollo del proyecto, incluyendo el backend, frontend y modelos de IA.

### 🛠 Tecnologías Utilizadas
- Frontend: Vue.js 3 + Nuxt.js 3 + Vuetify.js 3
- Backend: Python.
- IA/ML:
  - Generación de texto con modelos LLM (gemma3)
  - Detección de objetos y labels (Google Vision API)
- Gestión de Contenidos: Strapi (CMS Headless)
- Comunidad y Feedback: Discourse (foro integrado)
- Base de datos: PostgreSQL.
- Creación de Base de datos: Azure SQL (ODBC).

### 🎯 Características Principales
- 📷 Clasificación Automática de dinosaurios a partir de fotografías.
- 🧠 Descripciones Generadas por IA con información educativa y datos históricos.
- 🗣 Interfaz Interactiva para explorar y aprender sobre cada especie.
- 🌐 Foro de Comunidad para compartir descubrimientos y participar en debates.
- 📊 Dashboard de Administración para gestionar especies, datos y retroalimentación.
- 🧪 Entrenamiento Personalizado con datasets propios o subidos por la comunidad.

### 🚀 Instalación y Ejecución Local
```
# Clonar el repositorio
git clone https://github.com/Juandiego001/dinosaurs-ai.git
cd dinosaurs-ai

# Instalar dependencias del frontend (Nuxt)
cd frontend
yarn install

# Configurar variables de entorno de backend, strapi y discourse
NUXT_APP_URL='<ip-backend>'
NUXT_STRAPI_URL='<ip-strapi>'
NUXT_DISCOURSE_URL='<ip-discourse>'

# Ejecutar la app en desarrollo
yarn run dev

# En otra terminal

# Crear entorno virtual
cd ../backend
python -m venv venv

# Activar el entorno virtual
source venv/Scripts/activate

# Instalar dependencias del backend
pip install -r requirements.txt

# Configurar variables de entorno de bases de datos y demás
HOST='0.0.0.0'
SQLALCHEMY_DATABASE_URI='<ip-postgres>'
SQL_SERVER_DRIVER='<ip-sql-server>'

# Agregar archivo de credenciales de Google Vision a nivel raiz !IMPORTANTE
# /backend/<archivo-credenciales-google-vision.json>

# Ejecutar backend
python run.py
```


### 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Puedes colaborar de las siguientes formas:
- Hacerle un fork al repositorio para implementar mejoras y queden en tu repositorio.
- Haciendo pull requests con correcciones o nuevas features.
- Compartiendo datasets de dinosaurios.
- Ayudando con la documentación o traducciones.
