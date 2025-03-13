import sqlite3

# Conexión a la base de datos
def conectar_bd():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Crear tabla si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        password_hash BLOB NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()
