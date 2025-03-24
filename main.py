import os
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import time
import sys
from datetime import datetime
from plyer import notification

def run_command(command, cwd=None):
    """Ejecuta un comando y muestra la salida en la terminal de la GUI."""
    try:
        process = subprocess.Popen(command, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in process.stdout:
            terminal_text.insert(tk.END, line)
            terminal_text.see(tk.END)
            terminal_text.update_idletasks()

        for line in process.stderr:
            terminal_text.insert(tk.END, f"❌ {line}")
            terminal_text.see(tk.END)
            terminal_text.update_idletasks()

        process.wait()

    except Exception as e:
        terminal_text.insert(tk.END, f"Error: {e}\n")

def install_dependencies(project_path, framework):
    """Instala dependencias y configura ESLint y Prettier."""
    os.chdir(project_path)

    dependencies = [
        "react-icons", "axios", "dotenv", "zustand",
        "react-toastify", "clsx", "framer-motion",
        "@mui/material @emotion/react @emotion/styled"
    ]

    dev_dependencies = [
        "eslint", "prettier", "eslint-config-prettier",
        "eslint-plugin-react", "eslint-plugin-react-hooks"
    ]

    update_progress(40)
    run_command(f"npm install {' '.join(dependencies)}")
    
    update_progress(60)
    run_command(f"npm install -D {' '.join(dev_dependencies)}")
    
    update_progress(80)
    if framework == "next":
        run_command("npm install next-auth @next/font")

    setup_eslint_prettier(project_path)
    
    update_progress(100)
    terminal_text.insert(tk.END, "✅ Instalación completada.\n")

def setup_eslint_prettier(project_path):
    """Crea archivos de configuración de ESLint y Prettier."""
    eslint_config = """{
    "extends": ["react-app", "react-app/jest", "prettier"],
    "rules": {
        "prettier/prettier": ["error"],
        "react/react-in-jsx-scope": "off"
    }
}"""

    prettier_config = """{
    "semi": false,
    "singleQuote": true,
    "printWidth": 80
}"""

    with open(os.path.join(project_path, ".eslintrc.json"), "w") as eslint_file:
        eslint_file.write(eslint_config)

    with open(os.path.join(project_path, ".prettierrc"), "w") as prettier_file:
        prettier_file.write(prettier_config)

    terminal_text.insert(tk.END, "✔ ESLint y Prettier configurados.\n")

def update_progress(value):
    """Actualiza la barra de progreso."""
    progress_bar.set(value / 100)
    root.update_idletasks()

def create_project():
    """Crea el proyecto en un hilo separado para no congelar la interfaz."""
    def worker():
        project_name = entry_project_name.get().strip().lower().replace(" ", "-")
        project_path = entry_directory.get()

        if not project_name or not project_path:
            messagebox.showwarning("Advertencia", "Debes completar todos los campos.")
            return

        full_path = os.path.join(project_path, project_name)
        framework = framework_var.get()
        terminal_text.insert(tk.END, f"📦 Creando proyecto {project_name}...\n")
        update_progress(10)

        if framework == "React (Vite)":
            run_command(f"npm create vite@latest {full_path} -- --template react")
        elif framework == "Next.js":
            run_command(f"npx create-next-app@latest {full_path}")
        elif framework == "React (CRA)":
            run_command(f"npx create-react-app {full_path}")
        else:
            messagebox.showerror("Error", "Debes seleccionar un framework.")
            return

        update_progress(30)
        install_dependencies(full_path, framework)

        update_progress(100)
        terminal_text.insert(tk.END, f"✅ Proyecto {project_name} creado con éxito.\n")

        # Notificación al sistema operativo
        notification.notify(
            title="Proyecto Creado",
            message=f"El proyecto {project_name} se ha creado exitosamente.",
            timeout=10  # Duración en segundos
        )

        # Abrir la carpeta del proyecto automáticamente
        if sys.platform == "win32":
            os.startfile(full_path)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", full_path])
        else:
            subprocess.Popen(["xdg-open", full_path])

    threading.Thread(target=worker, daemon=True).start()

def select_directory():
    """Abre un cuadro de diálogo para seleccionar la carpeta donde crear el proyecto."""
    directory = filedialog.askdirectory()
    entry_directory.delete(0, tk.END)
    entry_directory.insert(0, directory)

def show_info():
    """Muestra la información del programa en una ventana personalizada."""
    info_window = ctk.CTkToplevel(root)
    info_window.title("Información del Programa")
    info_window.geometry("400x300")
    info_window.resizable(False, False)  # Evitar redimensionamiento de la ventana
    info_window.attributes("-topmost", True)  # Mantener la ventana encima de la principal
    info_window.protocol("WM_DELETE_WINDOW", lambda: close_info_window(info_window))  # Bloquear interacción con la ventana principal

    # Deshabilitar la ventana principal
    root.attributes("-disabled", True)

    # Etiquetas de información
    label_info_title = ctk.CTkLabel(info_window, text="Reactify 💻 1.0", font=("Arial", 16, "bold"))
    label_info_title.pack(pady=10)

    label_info_text = ctk.CTkLabel(info_window, text=(
        "Este programa permite crear proyectos React con los frameworks:\n"
        "- React (Vite)\n"
        "- Next.js\n"
        "- React (CRA)\n\n"
        "Incluye la instalación de dependencias y configuración de ESLint y Prettier."
    ), font=("Arial", 12), justify="left", anchor="w", wraplength=360)  # Ajustar el texto
    label_info_text.pack(pady=10, padx=20)

    # Botón de cerrar
    close_button = ctk.CTkButton(info_window, text="Cerrar", command=lambda: close_info_window(info_window))
    close_button.pack(pady=20)

def close_info_window(info_window):
    """Cierra la ventana de información y habilita la ventana principal."""
    info_window.destroy()
    root.attributes("-disabled", False)  # Habilitar la ventana principal nuevamente

# Configuración de la interfaz
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Reactify 1.0")
root.geometry("600x550")
root.resizable(False, False)
root.iconbitmap(r"C:\Users\jonyp\Desktop\logo.ico")

# Botón de información en la esquina superior derecha
btn_info = ctk.CTkButton(root, text="ℹ", command=show_info, width=30)
btn_info.place(x=560, y=10)

# Etiqueta y entrada para el nombre del proyecto
label_project_name = ctk.CTkLabel(root, text="Nombre del Proyecto:")
label_project_name.pack(pady=5)
entry_project_name = ctk.CTkEntry(root, width=400)
entry_project_name.pack(pady=5)

# Botón y entrada para seleccionar directorio
label_directory = ctk.CTkLabel(root, text="Seleccionar Carpeta:")
label_directory.pack(pady=5)
frame_directory = ctk.CTkFrame(root)
frame_directory.pack(pady=5)

entry_directory = ctk.CTkEntry(frame_directory, width=300)
entry_directory.pack(side="left", padx=5)
btn_directory = ctk.CTkButton(frame_directory, text="📂", width=30, command=select_directory)
btn_directory.pack(side="left")

# Selección del framework
label_framework = ctk.CTkLabel(root, text="Selecciona el Framework:")
label_framework.pack(pady=5)
framework_var = ctk.StringVar(value="React (Vite)")
framework_options = ["React (Vite)", "Next.js", "React (CRA)"]
framework_dropdown = ctk.CTkComboBox(root, values=framework_options, variable=framework_var)
framework_dropdown.pack(pady=5)

# Botón para crear el proyecto
btn_create = ctk.CTkButton(root, text="Crear Proyecto", command=create_project)
btn_create.pack(pady=10)

# Barra de progreso
progress_bar = ctk.CTkProgressBar(root, width=400)
progress_bar.set(0)  # Inicializa en 0%
progress_bar.pack(pady=10)

# Terminal integrada en la interfaz
terminal_frame = ctk.CTkFrame(root, height=200)
terminal_frame.pack(fill="both", expand=True, padx=10, pady=10)

terminal_text = tk.Text(terminal_frame, wrap="word", height=10, bg="black", fg="white", font=("Courier", 10))
terminal_text.pack(fill="both", expand=True, padx=5, pady=5)

# Copyright y año automático
current_year = datetime.now().year
label_copyright = ctk.CTkLabel(root, text=f"© Reactify {current_year} Johnny13. Todos los derechos reservados.", font=("Arial", 10))
label_copyright.pack(side="bottom", pady=10)

root.mainloop()
