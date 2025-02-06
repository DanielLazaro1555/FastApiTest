# 🛒 FastAPI Product API

## 📌 Descripción

Este proyecto es una API desarrollada con **FastAPI** que permite gestionar productos en una lista. Se pueden realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los productos. Se ha implementado validación de datos con **Pydantic** para garantizar que los productos cumplan con ciertas restricciones.

---

## 🚀 Tecnologías utilizadas

- **FastAPI** - Framework web para construir APIs rápidas y eficientes en Python.
- **Pydantic** - Para la validación de datos y la definición del esquema de los productos.
- **Uvicorn** - Servidor ASGI para ejecutar la API.
- **Python 3.10+** - Lenguaje de programación utilizado.

---

Crear un entorno virtual

python3 -m venv venv
source venv/bin/activate # En Linux/macOS
venv\Scripts\activate # En Windows

## 📌 Endpoints Disponibles

| Método   | Endpoint                     | Descripción                         |
| -------- | ---------------------------- | ----------------------------------- |
| `GET`    | `/`                          | Mensaje de bienvenida               |
| `GET`    | `/products`                  | Obtiene la lista de productos       |
| `GET`    | `/products/{id}`             | Obtiene un producto por su ID       |
| `GET`    | `/products/?stock=x&price=y` | Filtra productos por stock y precio |
| `POST`   | `/products`                  | Crea un nuevo producto              |
| `PUT`    | `/products/{id}`             | Actualiza un producto existente     |
| `DELETE` | `/products/{id}`             | Elimina un producto por su ID       |
