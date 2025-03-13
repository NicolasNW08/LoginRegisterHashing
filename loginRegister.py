import sqlite3
from tkinter import messagebox
import bcrypt

# Registrar el usuario
def registrar_usuario(entry_usuario, entry_password):
    usuario = entry_usuario.get()
    password = entry_password.get()

    if not usuario or not password:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    # Hash de la contraseña con bcrypt
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    #=======================================================================================================================
    # Ahora mismo la contraseña se acaba de hashear y se le añadio un "salt" como otra capa de seguridad de la contraseña.
    # README para mas información.
    #=======================================================================================================================

    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)", (usuario, password_hash))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Éxito", "Usuario registrado correctamente")
        entry_usuario.delete(0, "end")
        entry_password.delete(0, "end")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El usuario ya existe")
        entry_usuario.delete(0, "end")
        entry_password.delete(0, "end")


# Iniciar sesión
def iniciar_sesion(entry_usuario, entry_password):
    usuario = entry_usuario.get()
    password = entry_password.get()

    if not usuario or not password:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT password_hash FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    
    conn.close()

    if resultado:
        password_hash = resultado[0]
        
        # Verificación de la contraseña en la DB
        if bcrypt.checkpw(password.encode(), password_hash):
            messagebox.showinfo("Bienvenido", f"Hola, {usuario}!")
            entry_usuario.delete(0, "end")
            entry_password.delete(0, "end")
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")
            entry_password.delete(0, "end")
    else:
        messagebox.showerror("Error", "Usuario no encontrado")
        entry_usuario.delete(0, "end")
        entry_password.delete(0, "end")
        
        #=======================================================================================================================
        # Se verifica la contraseña el checkpw de bcrypt.
        # README para mas información.
        #=======================================================================================================================
