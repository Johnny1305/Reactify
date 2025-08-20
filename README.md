# Reactify 🚀

<div align="center">

![Reactify Logo](https://media.licdn.com/dms/image/v2/D4D22AQHtU82_E_mb_Q/feedshare-shrink_2048_1536/B4DZjDT_xdH0As-/0/1755623456664?e=1758758400&v=beta&t=88RGh9AJzmr7Tr19qAzt82Stx5sqYw18O5H-cRSAUzA)

**Una herramienta GUI intuitiva para crear proyectos React con configuración automática**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Version](https://img.shields.io/badge/Version-1.2-orange.svg)](https://github.com/Johnny1305/Reactify/releases)

[🐛 Reportar Bug](https://github.com/Johnny1305/Reactify/issues) • [💡 Solicitar Feature](https://github.com/Johnny1305/Reactify/issues)

</div>


## 🌟 Características Principales

### ⚡ Creación Rápida de Proyectos
- **React (Vite)** - La opción más moderna y rápida
- **Next.js** - Para aplicaciones full-stack
- **React (Create React App)** - El clásico confiable

### 🎯 Configuración Automática
- ✅ **TypeScript** opcional con un clic
- ✅ **ESLint + Prettier** preconfigurados
- ✅ **Dependencias esenciales** instaladas automáticamente
- ✅ **Estructura de carpetas** optimizada

### 📦 Gestión Inteligente de Dependencias
- **Dependencias Populares**: Lista curada de las librerías más usadas
- **Búsqueda en Tiempo Real**: Busca cualquier paquete de npm
- **Gestión de Versiones**: Selecciona versiones específicas
- **Instalación Automática**: Todo se instala sin intervención manual

### 🎨 Interfaz Moderna
- **Tema Oscuro**: Interfaz elegante y moderna
- **Terminal Integrada**: Ve el progreso en tiempo real
- **Notificaciones**: Alertas del sistema cuando termine


## 📋 Requisitos del Sistema

### Mínimos
- **Windows 10/11** (ejecutable compilado)
- **Node.js 14+** y **npm**

### Recomendados
- **Node.js 16+** y **npm/yarn**
- **4GB RAM** mínimo
- **Conexión a Internet** (para descargar dependencias)
- **Git** instalado (opcional, para algunas funcionalidades)

## 🚀 Instalación

### 📥 Descarga Directa (Recomendado)
Reactify está disponible como ejecutable independiente que **no requiere instalación de Python**.

1. Ve a la página de [**Releases**](https://github.com/Johnny1305/Reactify/releases/latest)
2. Descarga `Reactify.exe` 
3. Ejecuta el archivo directamente
4. ¡Listo para usar!

> **Nota**: Windows puede mostrar una advertencia de seguridad la primera vez. Haz clic en "Más información" → "Ejecutar de todas formas"


## 📖 Uso

### 1. 🏗️ Crear un Nuevo Proyecto

1. **Nombre del Proyecto**: Introduce un nombre (se convertirá en kebab-case)
2. **Carpeta de Destino**: Selecciona dónde crear el proyecto
3. **Framework**: Elige entre React (Vite), Next.js, o CRA
4. **TypeScript**: Marca la casilla si lo deseas
5. **Haz clic en "Crear Proyecto"**

### 2. 📦 Gestionar Dependencias

#### Dependencias Populares
Selecciona de la lista curada:
- **UI**: `@mui/material`, `ant-design`, `daisyui`
- **Estado**: `redux`, `zustand`, `recoil`
- **Formularios**: `formik`, `react-hook-form`
- **Routing**: `react-router-dom`
- **Estilos**: `tailwindcss`, `sass`, `bootstrap`

#### Búsqueda Personalizada
1. Usa el campo de búsqueda 🔍
2. Escribe el nombre de cualquier paquete npm
3. Selecciona de los resultados en tiempo real
4. Se agregará automáticamente a tu lista

### 3. ⚙️ Configuraciones Avanzadas

#### Selección de Versiones
- Cada dependencia permite elegir versiones específicas
- Se obtienen automáticamente desde npm
- Por defecto usa la versión `latest`

#### Terminal Integrada
- Ve el progreso de instalación en tiempo real
- Errores y warnings se muestran claramente
- Logs completos de npm y git


## 🛠️ Arquitectura del Proyecto

### Frameworks Soportados

| Framework | Comando | TypeScript | Características |
|-----------|---------|------------|----------------|
| **React (Vite)** | `npm create vite@latest` | ✅ | Rápido, HMR, ESM |
| **Next.js** | `npx create-next-app@latest` | ✅ | SSR, API routes, optimizado |
| **Create React App** | `npx create-react-app` | ✅ | Configuración zero, estable |

### Dependencias Incluidas por Defecto
```json
{
  "dependencies": {
    "react-icons": "^4.x",
    "axios": "^1.x", 
    "dotenv": "^16.x",
    "react-toastify": "^9.x",
    "clsx": "^1.x",
    "framer-motion": "^10.x"
  },
  "devDependencies": {
    "eslint": "^8.x",
    "prettier": "^2.x",
    "eslint-config-prettier": "^8.x",
    "eslint-plugin-react": "^7.x",
    "eslint-plugin-react-hooks": "^4.x"
  }
}
```


## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
# .env (creado automáticamente)
REACT_APP_API_URL=http://localhost:3000
REACT_APP_VERSION=1.0.0
```

### Configuración ESLint
```json
{
  "extends": [
    "react-app",
    "react-app/jest",
    "prettier"
  ],
  "rules": {
    "react/prop-types": "off",
    "no-unused-vars": "warn"
  }
}
```

### Configuración Prettier
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2
}
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor lee nuestra [guía de contribución](CONTRIBUTING.md).

### 🐛 Reportar Bugs
1. Busca si el bug ya existe en [Issues](https://github.com/Johnny1305/Reactify/issues)
2. Si no existe, crea uno nuevo con:
   - **Descripción clara** del problema
   - **Pasos para reproducir**
   - **Capturas de pantalla** si aplica
   - **Información del sistema** (SO, Python, Node.js)

### 💡 Solicitar Features
1. Revisa las [discusiones existentes](https://github.com/Johnny1305/Reactify/discussions)
2. Crea una nueva issue con:
   - **Descripción detallada** de la funcionalidad
   - **Casos de uso** específicos
   - **Mockups o ejemplos** si es posible

### 🔨 Desarrollo Local

```bash
# 1. Fork el repositorio
# 2. Clonar tu fork
git clone https://github.com/TU_USUARIO/Reactify.git

# 3. Crear rama para tu feature
git checkout -b feature/nueva-funcionalidad

# 4. Hacer cambios y commit
git commit -m "feat: agregar nueva funcionalidad"

# 5. Push y crear Pull Request
git push origin feature/nueva-funcionalidad
```


## 📌 Reactify – Changelog

### v1.3
- ✅ Búsqueda de dependencias mejorada con resultados en tiempo real desde npm.  
- ✅ Interfaz adaptativa: ventana ajustada automáticamente al tamaño de pantalla.  
- ✅ ComboBox de frameworks en modo solo lectura (evita escribir valores inválidos).  
- ✅ Correcciones de estabilidad y optimización general del rendimiento.  
- ✅ Preparación para el futuro sistema de **Auto-Setup de proyectos inteligentes** (planeado para v1.4).  

### v1.2
- ✅ Gestión de dependencias personalizadas con eliminación individual.  
- ✅ Terminal mejorada con mejor visualización.  
- ✅ Notificaciones del sistema multiplataforma.  

### v1.1
- ✅ Comprobación de actualizaciones añadida para notificar a los usuarios de nuevas versiones.  
- ✅ Instalación opcional de dependencias como *tailwindcss*, *react-hook-form* y *zustand* al crear proyectos.  

### v1.0
- 🚀 Lanzamiento inicial de Reactify, con soporte para la creación de proyectos React utilizando diferentes frameworks (Vite, CRA, Next.js).  


---

## 🎉 Reconocimientos

### 💝 Apoya el Proyecto
Si Reactify te ha sido útil, considera:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/johnny1305)

### 👥 Contribuidores

<!-- Esto se actualiza automáticamente -->
<a href="https://github.com/Johnny1305/Reactify/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Johnny1305/Reactify" />
</a>

### 🛠️ Construido Con
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern GUI framework
- [Requests](https://requests.readthedocs.io/) - HTTP library for Python
- [Plyer](https://github.com/kivy/plyer) - Cross-platform notifications
- [Win10Toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications) - Windows notifications


## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.


## 📞 Contacto

**Johnny1305** - [@johnny1305](https://github.com/Johnny1305)

**Proyecto**: [https://github.com/Johnny1305/Reactify](https://github.com/Johnny1305/Reactify)

**Reportar Issues**: [https://github.com/Johnny1305/Reactify/issues](https://github.com/Johnny1305/Reactify/issues)

---

<div align="center">

**⭐ ¡No olvides dar una estrella si te gustó el proyecto! ⭐**

</div>