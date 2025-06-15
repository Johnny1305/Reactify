import os
import subprocess
import threading
import json
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from datetime import datetime
from plyer import notification
from win10toast import ToastNotifier
import requests
import webbrowser

def check_for_updates():
    try:
        # URL de la API de GitHub para obtener la última versión
        github_api_url = "https://api.github.com/repos/Johnny1305/Reactify/releases/latest"  # Cambiar 'usuario' y 'repositorio'

        # Hacemos la solicitud GET
        response = requests.get(github_api_url)
        response.raise_for_status()  # Esto lanzará una excepción si la solicitud falla

        # Obtener la última versión de la respuesta JSON
        latest_version = response.json().get("tag_name")  # El campo "tag_name" tiene la versión

        # Versión actual del programa (cambiar esta versión a la versión real)
        current_version = "1.2"  # Aquí debe ir la versión actual de tu programa

        # Normalizar las versiones eliminando el prefijo "v" si lo tiene
        latest_version = latest_version.lstrip("v")
        current_version = current_version.lstrip("v")

        # Comparar versiones
        if latest_version != current_version:
            # Crear notificación de alta prioridad en Windows
            toaster = ToastNotifier()
            toaster.show_toast(
                "¡Actualización importante disponible!",
                f"Hay una nueva versión disponible: {latest_version}",
                duration=10,  # Duración de la notificación en segundos
                icon_path="logo.ico",  # Agrega un ícono si lo deseas
                threaded=True  # Hace que la notificación se muestre en segundo plano
            )
            terminal_text.insert(tk.END, f"🔔 ¡Nueva versión disponible: {latest_version}!\n")
        else:
            terminal_text.insert(tk.END, "✅ Estás en la última versión.\n")
    
    except Exception as e:
        terminal_text.insert(tk.END, f"❌ Error al comprobar actualizaciones: {e}\n")



def run_command(command, cwd=None):
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

def get_versions_async(package_name, callback):
    def worker():
        try:
            result = subprocess.run(f"npm view {package_name} versions --json", shell=True, capture_output=True, text=True)
            versions = json.loads(result.stdout)
            callback(versions[-10:] if len(versions) > 15 else versions)  # Últimas 10 versiones
        except Exception:
            callback(["latest"])

    threading.Thread(target=worker, daemon=True).start()

def install_dependencies(project_path, framework):
    os.chdir(project_path)

    dependencies = [
        "react-icons", "axios", "dotenv",
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

    selected_extras = [
        f"{dep}@{var.get()}" for dep, var in version_vars.items() if dep in extra_dependencies and extra_dependencies[dep].get()
    ]

    if selected_extras:
        terminal_text.insert(tk.END, f"📦 Instalando: {', '.join(selected_extras)}...\n")
        run_command(f"npm install {' '.join(selected_extras)}")

    update_progress(80)
    if framework == "Next.js":
        run_command("npm install next-auth @next/font")

    update_progress(100)
    terminal_text.insert(tk.END, "✅ Instalación completada.\n")
    
    # Dependencias TypeScript si está activado
    if use_typescript.get():
        terminal_text.insert(tk.END, "🛠️ Configurando TypeScript...\n")
        ts_dev_dependencies = [
            "typescript", "@types/react", "@types/react-dom"
        ]
        run_command(f"npm install -D {' '.join(ts_dev_dependencies)}")

def update_progress(value):
    progress_bar.set(value / 100)
    root.update_idletasks()

def create_project():
    def worker():
        project_name = entry_project_name.get().strip().lower().replace(" ", "-")
        project_path = entry_directory.get()

        if not project_name or not project_path:
            messagebox.showwarning("Advertencia", "Debes completar todos los campos.")
            return

        full_path = os.path.join(project_path, project_name)
        framework = framework_var.get()
        terminal_text.insert(tk.END, f"📦 Creando {project_name}...\n")
        update_progress(10)

        if framework == "React (Vite)":
            template = "react-ts" if use_typescript.get() else "react"
            run_command(f"npm create vite@latest {full_path} -- --template {template}")
        elif framework == "Next.js":
            run_command(f"npx create-next-app@latest {full_path}{' --typescript' if use_typescript.get() else ''}")
        elif framework == "React (CRA)":
            run_command(f"npx create-react-app {full_path}{' --template typescript' if use_typescript.get() else ''}")
        else:
            messagebox.showerror("Error", "Selecciona un framework.")
            return

        update_progress(30)
        install_dependencies(full_path, framework)

        update_progress(100)
        terminal_text.insert(tk.END, f"✅ Proyecto {project_name} creado.\n")

        notification.notify(
            title="Proyecto Creado",
            message=f"{project_name} se ha creado.",
            timeout=10
        )

        os.startfile(full_path) if os.name == "nt" else subprocess.Popen(["xdg-open", full_path])

    threading.Thread(target=worker, daemon=True).start()

def select_directory():
    directory = filedialog.askdirectory()
    entry_directory.delete(0, tk.END)
    entry_directory.insert(0, directory)


GITHUB_API_URL = f"https://api.github.com/repos/Johnny1305/Reactify/contributors"
def fetch_contributors():
    """Obtiene la lista de contribuidores desde la API de GitHub."""
    try:
        response = requests.get(GITHUB_API_URL)
        if response.status_code == 200:
            contributors = response.json()
            return [contributor["login"] for contributor in contributors]
        else:
            return ["Error al obtener contribuidores"]
    except Exception as e:
        return [f"Error: {str(e)}"]

def show_info():
    """Muestra la información del programa en una ventana personalizada."""
    info_window = ctk.CTkToplevel(root)
    info_window.title("Información del Programa")
    info_window.geometry("400x300")
    info_window.iconbitmap(r"C:\Users\jonyp\Desktop\Reactify\logo.ico")
    info_window.resizable(False, False)  # Evitar redimensionamiento de la ventana
    info_window.attributes("-topmost", True)  # Mantener la ventana encima de la principal
    info_window.protocol("WM_DELETE_WINDOW", lambda: close_info_window(info_window))  # Bloquear interacción con la ventana principal

    # Obtener las dimensiones de la pantalla
    screen_width = info_window.winfo_screenwidth()
    screen_height = info_window.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana de información
    x_position = int((screen_width - 400) / 2)
    y_position = int((screen_height - 300) / 2)

    # Establecer la posición en el centro
    info_window.geometry(f"400x300+{x_position}+{y_position}")

    # Etiquetas de información
    label_info_title = ctk.CTkLabel(info_window, text="Reactify 💻 1.2", font=("Arial", 16, "bold"))
    label_info_title.pack(pady=10)

    label_info_text = ctk.CTkLabel(info_window, text=(
        "Este programa permite crear proyectos React con los frameworks:\n"
        "- React (Vite)\n"
        "- Next.js\n"
        "- React (CRA)\n\n"
        "Incluye la instalación de dependencias y configuración de ESLint y Prettier."
    ), font=("Arial", 12), justify="left", anchor="w", wraplength=360)  # Ajustar el texto
    label_info_text.pack(pady=10, padx=20)

    # Obtener y mostrar contribuidores
    contributors = fetch_contributors()
    label_contributors_title = ctk.CTkLabel(info_window, text="Contribuidores:", font=("Arial", 12, "bold"))
    label_contributors_title.pack(pady=(10, 0))
    
    for contributor in contributors:
        label_contributor = ctk.CTkLabel(info_window, text=f"- {contributor}", font=("Arial", 12), justify="left")
        label_contributor.pack(anchor="w", padx=20)

    # Copyright y año automático
    current_year = datetime.now().year
    label_copyright = ctk.CTkLabel(info_window, text=f"© Reactify {current_year} Johnny13. Todos los derechos reservados.", font=("Arial", 12))
    label_copyright.pack(side="bottom", pady=10)

    # Botón de cerrar
    close_button = ctk.CTkButton(info_window, text="Cerrar", command=lambda: close_info_window(info_window))
    close_button.pack(pady=20)

def close_info_window(info_window):
    """Cierra la ventana de información y habilita la ventana principal."""
    info_window.destroy()
    root.attributes("-disabled", False)  # Habilitar la ventana principal nuevamente

# URL de tu página de donaciones en Buy Me a Coffee
DONATION_URL = "https://www.buymeacoffee.com/johnny1305"

# Función para abrir la ventana de donaciones
def open_donation_page():
    """Abre una ventana emergente con detalles sobre las donaciones."""
    donation_window = ctk.CTkToplevel(root)
    donation_window.title("Apoya el Proyecto 💖")
    donation_window.geometry("500x400")
    donation_window.resizable(False, False)
    donation_window.iconbitmap(r"C:\Users\jonyp\Desktop\Reactify\logo.ico")
    donation_window.attributes("-topmost", True)  # Mantener la ventana encima de la principal
    donation_window.protocol("WM_DELETE_WINDOW", lambda: close_info_window(donation_window))

    # Obtener las dimensiones de la pantalla
    screen_width = donation_window.winfo_screenwidth()
    screen_height = donation_window.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana de donaciones
    x_position = int((screen_width - 500) / 2)
    y_position = int((screen_height - 400) / 2)

    # Establecer la posición en el centro
    donation_window.geometry(f"500x400+{x_position}+{y_position}")


    # Encabezado con título y mensaje
    header = ctk.CTkLabel(
        donation_window, 
        text="🎁 ¡Gracias por tu apoyo!", 
        font=("Arial", 20, "bold")
    )
    header.pack(pady=10)

    subheader = ctk.CTkLabel(
        donation_window, 
        text="Cada donación ayuda a mejorar este proyecto y a mantenerlo activo.",
        wraplength=480,
        justify="center"
    )
    subheader.pack(pady=5)

    # Sección de uso de donaciones
    usos_frame = ctk.CTkFrame(donation_window)
    usos_frame.pack(pady=20, padx=10, fill="x")

    usos_label = ctk.CTkLabel(usos_frame, text="📌 ¿En qué se usarán las donaciones?", font=("Arial", 14, "bold"))
    usos_label.pack(pady=5)

    usos_texto = """
🔹 Desarrollo de nuevas funciones
🔹 Optimización y mejoras de rendimiento
🔹 Creación de contenido adicional
🔹 Soporte y mantenimiento continuo
🔹 Investigación y desarrollo
"""
    
    usos_info = ctk.CTkLabel(usos_frame, text=usos_texto, justify="left")
    usos_info.pack(padx=10, pady=(10, 20))


    # Botón oficial de Buy Me a Coffee
    donate_button = ctk.CTkButton(
        donation_window,
        text="☕ Buy Me a Coffee",
        fg_color="#FFDD00",
        text_color="black",
        font=("Arial", 16, "bold"),
        command=lambda: [webbrowser.open(DONATION_URL), donation_window.destroy(), root.attributes("-disabled", False)]
    )
    donate_button.pack(pady=20)

# Funciones del tooltip
def show_tooltip(event):
    global tooltip
    tooltip = ctk.CTkLabel(root, text="¡Haz una donación!", fg_color="gray20", text_color="white", corner_radius=5)
    tooltip.place(x=event.x_root - root.winfo_rootx() + 10, y=event.y_root - root.winfo_rooty() + 10)

def hide_tooltip(event):
    global tooltip
    tooltip.destroy()

# Fin de la función de tooltip

# Configuración de la interfaz
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Reactify 1.2")
root.geometry("750x600")
root.resizable(False, False)
root.iconbitmap(r"C:\Users\jonyp\Desktop\Reactify\logo.ico")

# Obtener las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x_position = int((screen_width - 750) / 2)
y_position = int((screen_height - 600) / 2)

# Establecer la posición en el centro
root.geometry(f"750x600+{x_position}+{y_position}")

# Botón de información en la esquina superior derecha
btn_info = ctk.CTkButton(root, text="ℹ", command=show_info, width=30, height=30)
btn_info.place(x=10, y=10)

# Botón de donación al lado del botón de información
btn_donate = ctk.CTkButton(root, text="♥", command=open_donation_page, width=30, height=30)
btn_donate.place(x=50, y=10)

# Eventos para mostrar y ocultar el tooltip
btn_donate.bind("<Enter>", show_tooltip)
btn_donate.bind("<Leave>", hide_tooltip)

# Título del proyecto
ctk.CTkLabel(root, text="Reactify🚀", font=("Arial", 20, "bold")).pack(pady=10)

# Entrada para el nombre del proyecto
ctk.CTkLabel(root, text="Nombre del Proyecto:").pack(pady=5)
entry_project_name = ctk.CTkEntry(root, width=400)
entry_project_name.pack(pady=5)

# Botón y entrada para seleccionar directorio
ctk.CTkLabel(root, text="Seleccionar Carpeta:").pack(pady=5)
frame_directory = ctk.CTkFrame(root)
frame_directory.pack(pady=5)

entry_directory = ctk.CTkEntry(frame_directory, width=300)
entry_directory.pack(side="left", padx=5)
ctk.CTkButton(frame_directory, text="📂", width=30, command=select_directory).pack(side="left")

# Selección del framework
ctk.CTkLabel(root, text="Selecciona el Framework:").pack(pady=5)
framework_var = ctk.StringVar(value="React (Vite)")
framework_dropdown = ctk.CTkComboBox(root, values=["React (Vite)", "Next.js", "React (CRA)"], variable=framework_var)
framework_dropdown.pack(pady=5)

use_typescript = tk.BooleanVar()
checkbox_typescript = ctk.CTkCheckBox(root, text="Usar TypeScript", variable=use_typescript)
checkbox_typescript.pack(pady=5)

# Botón para crear el proyecto
ctk.CTkButton(root, text="Crear Proyecto", command=create_project).pack(pady=10)

# Barra de progreso
progress_bar = ctk.CTkProgressBar(root, width=400)
progress_bar.set(0)  # Inicializa en 0%
progress_bar.pack(pady=10)

# Sección principal (Lista de dependencias + Terminal)
main_frame = ctk.CTkFrame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Frame de dependencias (con scroll)
dependencies_frame = ctk.CTkScrollableFrame(main_frame, width=350)
dependencies_frame.pack(side="left", fill="y", padx=5, pady=5)

ctk.CTkLabel(dependencies_frame, text="Dependencias Opcionales:").pack(pady=5)

extra_dependencies = {}
version_vars = {}
dropdown_menus = {}

def toggle_version_dropdown(dep, frame):
    if extra_dependencies[dep].get():
        def set_versions(versions):
            version_vars[dep].set(versions[-1])  # Última versión por defecto

            # Crear menú desplegable en la misma línea
            dropdown_menus[dep] = ctk.CTkComboBox(frame, values=versions, variable=version_vars[dep], width=120)
            dropdown_menus[dep].pack(side="right", padx=5)

        get_versions_async(dep, set_versions)
    else:
        if dep in dropdown_menus:
            dropdown_menus[dep].destroy()
            del dropdown_menus[dep]

dependencies_list = [
    "tailwindcss", "moralejas", "daisyui", "react-router-dom", "redux",
    "formik", "yup", "react-hook-form", "lodash",
    "recoil", "react-query", "zustand", "sass",
    "bootstrap", "ant-design", "react-select",
    "dayjs", "date-fns", "react-spring", "react-transition-group",
    "react-intersection-observer"
]

for dep in dependencies_list:
    extra_dependencies[dep] = tk.BooleanVar()
    version_vars[dep] = tk.StringVar()
    
    row_frame = ctk.CTkFrame(dependencies_frame)
    row_frame.pack(fill="x", padx=5, pady=2)

    ctk.CTkCheckBox(row_frame, text=dep, variable=extra_dependencies[dep], command=lambda d=dep, f=row_frame: toggle_version_dropdown(d, f)).pack(side="left")

# Terminal a la derecha
terminal_frame = ctk.CTkFrame(main_frame, width=400)
terminal_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

terminal_text = tk.Text(terminal_frame, wrap="word", bg="black", fg="white", font=("Courier", 10))
terminal_text.pack(fill="both", expand=True, padx=5, pady=5)

check_for_updates()
root.mainloop()
