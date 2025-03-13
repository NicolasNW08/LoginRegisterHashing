from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from loginRegister import iniciar_sesion, registrar_usuario

def gui_main():
    
    # Tamaño de la ventana  
    x = 650
    y = 700
    
    
    root = tk.Tk()
    root.title("LoginRegisterHashing")
    
    # Utilización de winfo_screenwidth y winfo_screenheight para centrar la ventana dependiendo del tamaño de la pantalla
    root.geometry("{}x{}+{}+{}".format(
            x, y,
            int((root.winfo_screenwidth() - x) / 2),
            int((root.winfo_screenheight() - y) / 2))
        )
    
    # ============================
    # README para mas información.
    # ============================
    
    root.resizable(False, False)
    root.configure(bg="#30373c")
    
    # frame todo pedorro
    frame = tk.LabelFrame(root, text="LoginRegister", bg="#5a6770", font=("Arial", 24, "bold"), foreground="white")
    frame.place(x=100, y=50, width=450, height=600, anchor="nw")
    
    # imagen 
    image = Image.open("img.png")
    image = image.resize((270, 270))
    image = ImageTk.PhotoImage(image)
    img = ttk.Label(frame, image=image, background="#5a6770")
    img.place(x=225, y=5, anchor="n")
    
    # Usuario
    usu_label = tk.Label(frame, text="Usuario:", font=("Arial", 20, "bold"),
                        background="#5a6770", foreground="white")
    usu_label.place(x=225, y=290, anchor="n")
    entry_usuario = tk.Entry(frame,font=("Arial", 18, "bold"))
    entry_usuario.place(x=225, y=330,anchor="n")
    
    # Contraseña
    con_label = tk.Label(frame, text="Contraseña:",font=("Arial", 20, "bold"),
                        background="#5a6770", foreground="white")
    con_label.place(x=225, y=370, anchor="n")
    entry_password = tk.Entry(frame, show="*",font=("Arial", 18, "bold"))
    entry_password.place(x=225, y=410,anchor="n")
    
    # Registro
    btn_registrar = tk.Button(frame, text="Registrar",font=("Arial", 18, "bold"), command=lambda: registrar_usuario(entry_usuario, entry_password))
    btn_registrar.place(x=225, y=450,anchor="n")

    # Login
    btn_login = tk.Button(frame, text="Iniciar Sesión",font=("Arial", 18, "bold"), command=lambda: iniciar_sesion(entry_usuario, entry_password))
    btn_login.place(x=225, y=505,anchor="n")
    
    root.mainloop()
    