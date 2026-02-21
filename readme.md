# Laboratorio de Vulnerabilidad Web: Inyección SQL (SQLi)

Este proyecto es una demostración educativa de una arquitectura web básica (Frontend + API + Base de datos) diseñada para ilustrar cómo ocurre una vulnerabilidad de **Inyección SQL (SQLi)** y cómo se implementa su solución mediante buenas prácticas de desarrollo.

## 🚀 Tecnologías Utilizadas

* **Frontend:** HTML5, CSS3 y Vanilla JavaScript (Fetch API).
* **Backend:** Python 3 y [FastAPI](https://fastapi.tiangolo.com/).
* **Base de Datos:** SQLite (integrado en Python).
* **Servidor ASGI:** Uvicorn.

## 📂 Estructura del Proyecto

El laboratorio consta de dos piezas principales:
1.  `main.py`: Contiene el servidor FastAPI, la inicialización de la base de datos SQLite con datos de prueba y los *endpoints* de búsqueda (uno vulnerable y uno seguro).
2.  `index.html`: Una interfaz de usuario simple que permite interactuar con la API para realizar las pruebas de inyección.

## ⚙️ API Endpoints

* `GET /`: Ruta de comprobación de estado del servidor.
* `GET /api/vulnerable_search?username={query}`: ❌ **Vulnerable**. Concatena directamente la entrada del usuario en la consulta SQL, permitiendo inyecciones.
* `GET /api/secure_search?username={query}`: ✅ **Seguro**. Utiliza consultas parametrizadas (Prepared Statements) para separar el código SQL de los datos proporcionados por el usuario.

## 🛠️ Cómo levantar el proyecto

Sigue estos pasos en tu terminal para iniciar el servidor local:

### 1. Activar el entorno virtual (Recomendado)
Si estás usando un entorno virtual (como se muestra en tu terminal con `(.venv)`), asegúrate de tenerlo activado.
```bash
# En Windows
.venv\Scripts\activate

# En macOS/Linux
source .venv/bin/activate
```

## instalar dependencias

pip install fastapi uvicorn

## inicializar servidor
uvicorn main:app --reload
```bash

#🧪 Cómo probar la vulnerabilidad
Prueba de control: Ingresa la palabra admin en el campo de texto y haz clic en cualquiera de los botones. Verás los datos de ese usuario.

El Ataque (Explotación): Ingresa la siguiente carga útil (payload) exacta en el buscador: ' OR '1'='1

Haz clic en Búsqueda Vulnerable: Verás que la base de datos devuelve todos los registros, exponiendo datos sensibles.

Haz clic en Búsqueda Segura: El sistema procesará la entrada correctamente como una cadena de texto inofensiva y devolverá un arreglo vacío [], mitigando el ataque.
