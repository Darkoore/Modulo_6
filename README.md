# 📌 Proyecto Modulo_6 - Gestión de Proyectos y Tareas con Django

## 📖 Descripción

Este proyecto es una aplicación web desarrollada con Django para el bootcamp de alkemy que permite a los usuarios registrarse, iniciar sesión y gestionar proyectos y tareas de manera eficiente.

Cada usuario puede:

* Crear, editar y eliminar proyectos.
* Crear tareas asociadas a cada proyecto.
* Visualizar el estado de sus tareas.

---

## ⚙️ Requisitos

Antes de comenzar, asegúrate de tener instalado:

* Python 3.x
* pip (gestor de paquetes)

---

## 🚀 Instalación

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

### 1. Clonar o descargar el proyecto

Ubícate en la carpeta donde deseas trabajar.

---

### 2. Crear entorno virtual

```bash
python -m venv venv
```

---

### 3. Activar entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

---

### 4. Instalar dependencias

```bash
pip install django
```

---

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

---

### 6. Crear superusuario (admin)

```bash
python manage.py createsuperuser
```

---

### 7. Ejecutar servidor

```bash
python manage.py runserver
```

---

### 8. Acceder al sistema

Abrir en navegador:

* Aplicación: http://127.0.0.1:8000/
* Panel admin: http://127.0.0.1:8000/admin/

---

## 🧑‍💻 Uso del sistema

### 🔐 Autenticación

* Registro de usuarios desde la página de login.
* Inicio y cierre de sesión.

---

### 📁 Gestión de proyectos

* Crear proyectos
* Editar proyectos
* Eliminar proyectos

---

### ✅ Gestión de tareas

* Crear tareas asociadas a un proyecto
* Visualizar tareas dentro de cada proyecto
* Marcar tareas como completadas

---

### ⚙️ Panel administrativo

* Gestión de usuarios
* Gestión de proyectos y tareas
* Filtros y búsqueda personalizada

---

## 🗂️ Estructura del proyecto

```text
Modulo_6/
│
├── Modulo_6/          # Configuración principal del proyecto
│
├── accounts/          # Gestión de usuarios (registro)
│   ├── views.py
│   ├── forms.py
│
├── projects/          # Lógica principal (proyectos y tareas)
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── tests.py
│
├── templates/         # Plantillas HTML
│   ├── base.html
│   ├── accounts/
│   ├── projects/
│
├── static/            # Archivos estáticos (CSS) [Falta implementar]
│
├── manage.py
```

---

## 🔒 Seguridad implementada

* Protección CSRF en formularios
* Restricción de acceso con autenticación
* Validación de datos mediante formularios y modelos

---

## 🧪 Pruebas

Para ejecutar las pruebas unitarias:

```bash
python manage.py test
```

Incluye pruebas para:

* Creación de proyectos
* Acceso autenticado
* Restricción de acceso sin login

---

## 📌 Tecnologías utilizadas

* Django
* Python
* HTML

---

## ☠️ SuperUsuario creado
usuario: admin
contraseña: admin
correo: admin@admin.cl
