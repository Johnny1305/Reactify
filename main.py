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
        github_api_url = "https://api.github.com/repos/Johnny1305/Reactify/releases/latest"
        response = requests.get(github_api_url)
        response.raise_for_status()
        
        latest_version = response.json().get("tag_name")
        current_version = "1.3"
        
        latest_version = latest_version.lstrip("v")
        current_version = current_version.lstrip("v")
        
        if latest_version != current_version:
            toaster = ToastNotifier()
            toaster.show_toast(
                "¡Actualización importante disponible!",
                f"Hay una nueva versión disponible: {latest_version}",
                duration=10,
                icon_path="logo.ico",
                threaded=True
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
            callback(versions[-10:] if len(versions) > 15 else versions)
        except Exception:
            callback(["latest"])

    threading.Thread(target=worker, daemon=True).start()

def search_packages_realtime(query, callback):
    def worker():
        try:
            if not query.strip() or len(query) < 2:
                callback([])
                return
            
            search_url = f"https://registry.npmjs.org/-/v1/search?text={query}&size=10"
            response = requests.get(search_url, timeout=3)
            
            if response.status_code == 200:
                data = response.json()
                packages = []
                for pkg in data.get('objects', []):
                    package_info = pkg.get('package', {})
                    name = package_info.get('name', '')
                    description = package_info.get('description', '')[:100] + "..." if len(package_info.get('description', '')) > 100 else package_info.get('description', '')
                    packages.append({
                        'name': name,
                        'description': description,
                        'version': package_info.get('version', 'latest')
                    })
                callback(packages)
            else:
                callback([])
        except Exception as e:
            print(f"Error searching packages: {e}")
            callback([])

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

    selected_extras = []
    
    for dep in extra_dependencies:
        if extra_dependencies[dep].get():
            version = version_vars[dep].get() if dep in version_vars and version_vars[dep].get() else "latest"
            selected_extras.append(f"{dep}@{version}")
    
    for dep in custom_dependencies:
        if custom_dependencies[dep]["enabled"].get():
            version = custom_dependencies[dep]["version"].get() if custom_dependencies[dep]["version"].get() else "latest"
            selected_extras.append(f"{dep}@{version}")

    if selected_extras:
        terminal_text.insert(tk.END, f"📦 Instalando: {', '.join(selected_extras)}...\n")
        run_command(f"npm install {' '.join(selected_extras)}")

    update_progress(80)
    if framework == "Next.js":
        run_command("npm install next-auth @next/font")

    update_progress(100)
    terminal_text.insert(tk.END, "✅ Instalación completada.\n")
    
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

def on_search_change(event=None):
    query = search_entry.get()
    
    if len(query) < 2:
        hide_search_results()
        return
    
    search_packages_realtime(query, display_search_results)

def display_search_results(packages):
    for widget in search_results_frame.winfo_children():
        widget.destroy()
    
    if not packages:
        hide_search_results()
        return
    
    # Calcular posición relativa al campo de búsqueda
    search_x = search_container.winfo_x() + dependencies_frame.winfo_x() + top_frame.winfo_x()
    search_y = search_container.winfo_y() + search_container.winfo_height() + dependencies_frame.winfo_y() + top_frame.winfo_y()
    
    search_results_frame.place(x=search_x, y=search_y)
    
    results_scrollable = ctk.CTkScrollableFrame(search_results_frame, height=180)
    results_scrollable.pack(fill="both", expand=True, padx=5, pady=5)
    
    for pkg in packages:
        result_frame = ctk.CTkFrame(results_scrollable)
        result_frame.pack(fill="x", padx=2, pady=2)
        
        name_label = ctk.CTkLabel(
            result_frame, 
            text=pkg['name'], 
            font=("Arial", 12, "bold"),
            cursor="hand2"
        )
        name_label.pack(anchor="w", padx=5, pady=2)
        
        if pkg['description']:
            desc_label = ctk.CTkLabel(
                result_frame, 
                text=pkg['description'], 
                font=("Arial", 10),
                wraplength=300,
                justify="left"
            )
            desc_label.pack(anchor="w", padx=5, pady=(0, 5))
        
        def select_package(package_name=pkg['name']):
            add_custom_dependency(package_name)
            search_entry.delete(0, tk.END)
            hide_search_results()
            terminal_text.insert(tk.END, f"✅ Dependencia '{package_name}' agregada correctamente.\n")
        
        result_frame.bind("<Button-1>", lambda e, pkg_name=pkg['name']: select_package(pkg_name))
        name_label.bind("<Button-1>", lambda e, pkg_name=pkg['name']: select_package(pkg_name))
        if pkg['description']:
            desc_label.bind("<Button-1>", lambda e, pkg_name=pkg['name']: select_package(pkg_name))
        
        def on_enter(e, frame=result_frame):
            frame.configure(fg_color=("#3B8ED0", "#1F6AA5"))
        
        def on_leave(e, frame=result_frame):
            frame.configure(fg_color=("#3a3a3a", "#212121"))
        
        result_frame.bind("<Enter>", on_enter)
        result_frame.bind("<Leave>", on_leave)
        name_label.bind("<Enter>", on_enter)
        name_label.bind("<Leave>", on_leave)
        if pkg['description']:
            desc_label.bind("<Enter>", on_enter)
            desc_label.bind("<Leave>", on_leave)

def hide_search_results():
    search_results_frame.place_forget()

def update_search_position():
    if search_results_frame.winfo_ismapped():
        root.after(10, lambda: display_search_results([]))

def add_custom_dependency(dep_name):
    if dep_name in custom_dependencies:
        messagebox.showinfo("Información", f"La dependencia '{dep_name}' ya está agregada.")
        return
    
    custom_dependencies[dep_name] = {
        "enabled": tk.BooleanVar(),
        "version": tk.StringVar(value="latest"),
        "frame": None,
        "dropdown": None
    }
    
    # Crear el frame para la nueva dependencia
    row_frame = ctk.CTkFrame(dependencies_frame)
    
    # Insertar AL PRINCIPIO de la lista, después del separador
    # Primero obtenemos todos los widgets hijos
    children = dependencies_frame.winfo_children()
    
    # Encontrar la posición del separador
    separator_index = -1
    for i, child in enumerate(children):
        if hasattr(child, '_name') and 'separator' in str(child):
            separator_index = i
            break
    
    # Si encontramos el separador, insertar después de él
    if separator_index != -1:
        # Desempacar el widget
        row_frame.pack(fill="x", padx=5, pady=2)
        # Mover el widget al principio (después del separador)
        row_frame.pack_forget()
        row_frame.pack(fill="x", padx=5, pady=2, after=children[separator_index])
    else:
        # Si no hay separador, añadir al principio
        row_frame.pack(fill="x", padx=5, pady=2)
        row_frame.pack_forget()
        # Obtener el primer elemento que sea un checkbox de dependencia
        first_dep_widget = None
        for child in children:
            if isinstance(child, ctk.CTkFrame) and any(isinstance(grandchild, ctk.CTkCheckBox) for grandchild in child.winfo_children()):
                first_dep_widget = child
                break
        
        if first_dep_widget:
            row_frame.pack(fill="x", padx=5, pady=2, before=first_dep_widget)
        else:
            row_frame.pack(fill="x", padx=5, pady=2)
    
    custom_dependencies[dep_name]["frame"] = row_frame
    
    # Crear checkbox con estilo diferenciado para dependencias personalizadas
    checkbox = ctk.CTkCheckBox(
        row_frame, 
        text=f"🔍 {dep_name} (personalizada)", 
        variable=custom_dependencies[dep_name]["enabled"],
        command=lambda: toggle_custom_version_dropdown(dep_name),
        text_color=("#00D4AA", "#00D4AA")  # Color especial para dependencias personalizadas
    )
    checkbox.pack(side="left")
    
    delete_btn = ctk.CTkButton(
        row_frame, 
        text="❌", 
        width=25, 
        height=25,
        command=lambda: remove_custom_dependency(dep_name),
        fg_color=("red", "darkred"),
        hover_color=("darkred", "red")
    )
    delete_btn.pack(side="right", padx=5)

def toggle_custom_version_dropdown(dep_name):
    if custom_dependencies[dep_name]["enabled"].get():
        def set_versions(versions):
            custom_dependencies[dep_name]["version"].set(versions[-1])
            
            dropdown = ctk.CTkComboBox(
                custom_dependencies[dep_name]["frame"], 
                values=versions, 
                variable=custom_dependencies[dep_name]["version"], 
                width=120
            )
            dropdown.pack(side="right", padx=(5, 10))
            custom_dependencies[dep_name]["dropdown"] = dropdown
        
        get_versions_async(dep_name, set_versions)
    else:
        if custom_dependencies[dep_name]["dropdown"]:
            custom_dependencies[dep_name]["dropdown"].destroy()
            custom_dependencies[dep_name]["dropdown"] = None

def remove_custom_dependency(dep_name):
    if dep_name in custom_dependencies:
        custom_dependencies[dep_name]["frame"].destroy()
        del custom_dependencies[dep_name]
        terminal_text.insert(tk.END, f"🗑️ Dependencia '{dep_name}' eliminada.\n")

GITHUB_API_URL = f"https://api.github.com/repos/Johnny1305/Reactify/contributors"
def fetch_contributors():
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
    info_window = ctk.CTkToplevel(root)
    info_window.title("Información del Programa")
    info_window.geometry("400x300")
    info_window.iconbitmap(r"C:\Users\jonyp\Desktop\Reactify\logo.ico")
    info_window.resizable(False, False)
    info_window.attributes("-topmost", True)
    info_window.protocol("WM_DELETE_WINDOW", lambda: close_info_window(info_window))

    screen_width = info_window.winfo_screenwidth()
    screen_height = info_window.winfo_screenheight()
    x_position = int((screen_width - 400) / 2)
    y_position = int((screen_height - 300) / 2)
    info_window.geometry(f"400x300+{x_position}+{y_position}")

    label_info_title = ctk.CTkLabel(info_window, text="Reactify 💻 1.3", font=("Arial", 16, "bold"))
    label_info_title.pack(pady=10)

    label_info_text = ctk.CTkLabel(info_window, text=(
        "Este programa permite crear proyectos React con los frameworks:\n"
        "- React (Vite)\n"
        "- Next.js\n"
        "- React (CRA)\n\n"
        "Incluye la instalación de dependencias y configuración de ESLint y Prettier."
    ), font=("Arial", 12), justify="left", anchor="w", wraplength=360)
    label_info_text.pack(pady=10, padx=20)

    contributors = fetch_contributors()
    label_contributors_title = ctk.CTkLabel(info_window, text="Contribuidores:", font=("Arial", 12, "bold"))
    label_contributors_title.pack(pady=(10, 0))
    
    for contributor in contributors:
        label_contributor = ctk.CTkLabel(info_window, text=f"- {contributor}", font=("Arial", 12), justify="left")
        label_contributor.pack(anchor="w", padx=20)

    current_year = datetime.now().year
    label_copyright = ctk.CTkLabel(info_window, text=f"© Reactify {current_year} Johnny13. Todos los derechos reservados.", font=("Arial", 12))
    label_copyright.pack(side="bottom", pady=10)

    close_button = ctk.CTkButton(info_window, text="Cerrar", command=lambda: close_info_window(info_window))
    close_button.pack(pady=20)

def close_info_window(info_window):
    info_window.destroy()
    root.attributes("-disabled", False)

DONATION_URL = "https://www.buymeacoffee.com/johnny1305"

def open_donation_page():
    donation_window = ctk.CTkToplevel(root)
    donation_window.title("Apoya el Proyecto 💖")
    donation_window.geometry("500x400")
    donation_window.resizable(False, False)
    donation_window.iconbitmap(r"C:\Users\jonyp\Desktop\Reactify\logo.ico")
    donation_window.attributes("-topmost", True)
    donation_window.protocol("WM_DELETE_WINDOW", lambda: close_info_window(donation_window))

    screen_width = donation_window.winfo_screenwidth()
    screen_height = donation_window.winfo_screenheight()
    x_position = int((screen_width - 500) / 2)
    y_position = int((screen_height - 400) / 2)
    donation_window.geometry(f"500x400+{x_position}+{y_position}")

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

    donate_button = ctk.CTkButton(
        donation_window,
        text="☕ Buy Me a Coffee",
        fg_color="#FFDD00",
        text_color="black",
        font=("Arial", 16, "bold"),
        command=lambda: [webbrowser.open(DONATION_URL), donation_window.destroy(), root.attributes("-disabled", False)]
    )
    donate_button.pack(pady=20)

def show_tooltip(event):
    global tooltip
    tooltip = ctk.CTkLabel(root, text="¡Haz una donación!", fg_color="gray20", text_color="white", corner_radius=5)
    tooltip.place(x=event.x_root - root.winfo_rootx() + 10, y=event.y_root - root.winfo_rooty() + 10)

def hide_tooltip(event):
    global tooltip
    tooltip.destroy()

def on_click_outside(event):
    widget_name = str(event.widget)
    search_widgets = [str(search_entry), str(search_results_frame), str(search_container)]
    
    if not any(widget_name.startswith(widget) for widget in search_widgets):
        hide_search_results()

def toggle_version_dropdown(dep, frame):
    if extra_dependencies[dep].get():
        def set_versions(versions):
            if dep not in version_vars:
                version_vars[dep] = tk.StringVar()
            version_vars[dep].set(versions[-1])

            dropdown_menus[dep] = ctk.CTkComboBox(frame, values=versions, variable=version_vars[dep], width=120)
            dropdown_menus[dep].pack(side="right", padx=5)

        get_versions_async(dep, set_versions)
    else:
        if dep in dropdown_menus:
            dropdown_menus[dep].destroy()
            del dropdown_menus[dep]

# Configuración de la interfaz
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Reactify 1.3")
root.geometry("1200x700")
root.iconbitmap(r"C:\Users\jonyp\Desktop\Reactify\logo.ico")

root.bind("<Button-1>", on_click_outside)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int((screen_width - 1200) / 2)
y_position = int((screen_height - 700) / 2)
root.geometry(f"1200x700+{x_position}+{y_position}")

# Botones de información y donación (posición fija)
btn_info = ctk.CTkButton(root, text="ℹ", command=show_info, width=30, height=30)
btn_info.place(x=10, y=10)

btn_donate = ctk.CTkButton(root, text="♥", command=open_donation_page, width=30, height=30)
btn_donate.place(x=50, y=10)

btn_donate.bind("<Enter>", show_tooltip)
btn_donate.bind("<Leave>", hide_tooltip)

# Título principal
title_label = ctk.CTkLabel(root, text="Reactify🚀", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# NUEVO LAYOUT: Frame principal dividido en dos secciones
top_frame = ctk.CTkFrame(root)
top_frame.pack(fill="both", expand=True, padx=10, pady=10)

# ===== LADO IZQUIERDO: DEPENDENCIAS =====
dependencies_frame = ctk.CTkScrollableFrame(top_frame, width=400)
dependencies_frame.pack(side="left", fill="both", expand=False, padx=(5, 10), pady=5)

ctk.CTkLabel(dependencies_frame, text="⚙️ Dependencias Opcionales", font=("Arial", 16, "bold")).pack(pady=5)

# Sección de búsqueda
search_container = ctk.CTkFrame(dependencies_frame)
search_container.pack(fill="x", padx=5, pady=10)

ctk.CTkLabel(search_container, text="🔍 Buscar dependencia en npm:").pack(pady=5)

search_entry = ctk.CTkEntry(
    search_container, 
    placeholder_text="Escribe para buscar (ej: material-ui)", 
    width=350
)
search_entry.pack(padx=10, pady=5)

search_entry.bind('<KeyRelease>', on_search_change)

# Frame para resultados de búsqueda (flotante)
search_results_frame = ctk.CTkFrame(root, width=380, height=200)


# Separador entre secciones
separator = ctk.CTkFrame(dependencies_frame, height=2, fg_color="gray")
separator.pack(fill="x", padx=5, pady=15)

# Variables para dependencias
extra_dependencies = {}
version_vars = {}
dropdown_menus = {}
custom_dependencies = {}

# Lista de dependencias predefinidas
dependencies_list = [
    "tailwindcss", "daisyui", "react-router-dom", "redux",
    "formik", "yup", "react-hook-form", "lodash",
    "recoil", "react-query", "zustand", "sass",
    "bootstrap", "ant-design", "react-select",
    "dayjs", "date-fns", "react-spring", "react-transition-group",
    "react-intersection-observer"
]

for dep in dependencies_list:
    extra_dependencies[dep] = tk.BooleanVar()
    
    row_frame = ctk.CTkFrame(dependencies_frame)
    row_frame.pack(fill="x", padx=5, pady=2)

    ctk.CTkCheckBox(row_frame, text=dep, variable=extra_dependencies[dep], command=lambda d=dep, f=row_frame: toggle_version_dropdown(d, f)).pack(side="left")

# ===== LADO DERECHO: CONFIGURACIÓN DEL PROYECTO =====
config_frame = ctk.CTkFrame(top_frame, width=500)
config_frame.pack(side="right", fill="both", expand=True, padx=(10, 5), pady=5)

# Título de configuración
ctk.CTkLabel(config_frame, text="🔧 Configuración del Proyecto", font=("Arial", 16, "bold")).pack(pady=15)

# Nombre del proyecto
ctk.CTkLabel(config_frame, text="Nombre del Proyecto:", font=("Arial", 12)).pack(pady=(10, 5))
entry_project_name = ctk.CTkEntry(config_frame, width=400)
entry_project_name.pack(pady=5)

# Selección de directorio
ctk.CTkLabel(config_frame, text="Seleccionar Carpeta:", font=("Arial", 12)).pack(pady=(15, 5))
frame_directory = ctk.CTkFrame(config_frame)
frame_directory.pack(pady=5)

entry_directory = ctk.CTkEntry(frame_directory, width=340)
entry_directory.pack(side="left", padx=5)
ctk.CTkButton(frame_directory, text="📂", width=40, command=select_directory).pack(side="left")

# Framework selection
ctk.CTkLabel(config_frame, text="Selecciona el Framework:", font=("Arial", 12)).pack(pady=(15, 5))
framework_var = ctk.StringVar(value="React (Vite)")
framework_dropdown = ctk.CTkComboBox(config_frame, values=["React (Vite)", "Next.js", "React (CRA)"], variable=framework_var, width=150)
framework_dropdown.pack(pady=5)
framework_dropdown.configure(state="readonly")

# TypeScript checkbox
use_typescript = tk.BooleanVar()
checkbox_typescript = ctk.CTkCheckBox(config_frame, text="Usar TypeScript", variable=use_typescript)
checkbox_typescript.pack(pady=15)

# Botón crear proyecto
create_button = ctk.CTkButton(config_frame, text="Crear Proyecto", command=create_project, height=40, font=("Arial", 14, "bold"))
create_button.pack(pady=20)

# Barra de progreso
progress_bar = ctk.CTkProgressBar(config_frame, width=400)
progress_bar.set(0)
progress_bar.pack(pady=10)

# ===== PARTE INFERIOR: TERMINAL =====
terminal_frame = ctk.CTkFrame(root, height=200)
terminal_frame.pack(fill="x", padx=10, pady=(0, 10))

terminal_text = tk.Text(
    terminal_frame, 
    wrap="word", 
    bg="black", 
    fg="white", 
    font=("Courier", 10),
    height=10
)
terminal_text.pack(fill="both", expand=True, padx=5, pady=(0, 5))

# Verificar actualizaciones al iniciar
check_for_updates()
root.mainloop()