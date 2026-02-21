# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# Configuración básica de CORS para que el frontend pueda consultar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "estado": "OK",
        "mensaje": "¡El servidor FastAPI está funcionando correctamente!",
        "documentacion": "Visita http://localhost:8000/docs para ver la API"
}

# Inicializar base de datos de prueba
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, secret_data TEXT)")
    # Insertar datos de prueba
    cursor.execute("INSERT OR IGNORE INTO users (id, username, secret_data) VALUES (1, 'admin', 'SuperSecreto_Admin')")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, secret_data) VALUES (2, 'invitado', 'SinSecretos')")
    conn.commit()
    conn.close()

init_db()

# ❌ CÓDIGO VULNERABLE
@app.get("/api/vulnerable_search")
def vulnerable_search(username: str):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # VULNERABILIDAD: Concatenación directa del input del usuario (f-strings)
    # Si el input es: ' OR '1'='1 
    # La query será: SELECT * FROM users WHERE username = '' OR '1'='1'
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()
        
    return {"data": result, "query_ejecutada": query}

# ✅ CÓDIGO SEGURO (SOLUCIÓN)
@app.get("/api/secure_search")
def secure_search(username: str):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # SOLUCIÓN: Uso de Consultas Parametrizadas (Prepared Statements)
    # El motor de la base de datos trata el input estrictamente como un dato (string),
    # escapando automáticamente cualquier caracter especial o intento de inyección.
    query = "SELECT * FROM users WHERE username = ?"
    
    cursor.execute(query, (username,))
    result = cursor.fetchall()
    conn.close()
    
    return {"data": result, "query_ejecutada": query}