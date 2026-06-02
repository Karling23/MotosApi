<div align="center">

<img src="https://ute.edu.ec/wp-content/uploads/2021/08/LogoUteTrans.png" alt="UTE - Escuela de Tecnologías" width="250"/>

</div>

<hr>
<br>

<div style="border-left: 4px solid #1e88e5; padding-left: 15px; margin-top: 20px;">

<p><strong>Universidad Tecnológica Equinoccial</strong></p>

<p><strong>Escuela de Tecnologías</strong></p>

<p><strong>Carrera:</strong> Desarrollo de Software</p>

<p><strong>Asignatura:</strong> Programación IV</p>

</div>

<br><br>

<p><strong>Tema:</strong> SEMINARIO DE INTEGRACIÓN - Construcción de Backend Django.</p>

<br>

<p><strong>Fecha:</strong> 03/06/2026</p>

<p><strong>Presentado por:</strong></p>

<ul>
  <li>Alquinga Carlos</li>
</ul>

<p><strong>Docente:</strong> Francisco Javier Higuera González </p>

<hr>

# MotosApi

MotosApi es una API desarrollada en Django REST Framework para la gestión de productos, usuarios y transacciones de una tienda de motocicletas y accesorios.

## Instalación y Ejecución del Backend

Sigue estos pasos para levantar el entorno de desarrollo en tu máquina local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Karling23/MotosApi.git
   cd MotosApi
   ```

2. **Crear y configurar postgres:**

    En Windows: abrir pgAdmin o usar la consola psql desde el menú de inicio

   ```bash
   CREATE USER motosapi_user WITH PASSWORD 'motosapi_pass';
   CREATE DATABASE motosapi_db OWNER motosapi_user;
   GRANT ALL PRIVILEGES ON DATABASE motosapi_db TO motosapi_user;
   ALTER USER motosapi_user CREATEDB;
   \q
   ```

3. **Crear y activar un entorno virtual:**
   ```bash
   # En Windows:
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. **Instalar dependencias:**
   ```bash
   uv pip install -r requirements.txt
   ```
   

5. **Configurar las variables de entorno:**
   `.env`
   ```bash
   # Django
    SECRET_KEY=django-insecure-change-this-in-production
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1

    # PostgreSQL
    DB_NAME=motosapi_db
    DB_USER=motosapi_user
    DB_PASSWORD=motosapi_pass
    DB_HOST=localhost
    DB_PORT=5432

    # CORS
    CORS_ALLOW_ALL_ORIGINS=True

    # Test database (Django la crea automáticamente)
    TEST_DB_NAME=motosapi_test_db
   ```

6. **Aplicar migraciones:**
   ```bash
   python manage.py migrate
   ```

7. **Crear superusuario (opcional pero recomendado):**
   ```bash
   python manage.py createsuperuser
   ```
   Username: admin |
   Email address: admin@motosapi.com |
   Password: Admin1234! 

8. **Ejecutar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
   La API estará disponible en `http://localhost:8000`.

---

## Ejemplos de uso de la API (con Token)

El sistema utiliza **JSON Web Tokens (JWT)** para la autenticación. 

### 1. Obtener el Token (Login)

Realiza una petición `POST` al endpoint de inicio de sesión con tus credenciales:

**Petición:**
```http
POST /api/auth/login/
Content-Type: application/json

{
    "username": "tu_usuario",
    "password": "tu_password"
}
```

**Respuesta Exitosa:**
```json
{
    "refresh": "eyJhbGciOiJIUzI...",
    "access": "eyJhbGciOiJIUzI..."
}
```

### 2. Usar el Token en peticiones protegidas

Para acceder a los endpoints protegidos (como el listado de pedidos), debes incluir el token en el encabezado `Authorization`.

**Petición en Postman:**
1. Ve a la pestaña **Authorization**.
2. Selecciona el tipo **Bearer Token**.
3. Pega tu `access_token` en el campo correspondiente.

---

## Listado de Endpoints

A continuación, se listan las rutas principales de la API. Se asume el prefijo `/api/` antes de cada endpoint.

### Autenticación (`/api/auth/`)
- `POST /register/` - Registrar nuevo usuario.
- `POST /login/` - Iniciar sesión (Obtener JWT).

### Usuarios (`/api/usuarios/`)
- `GET /` - Listar usuarios.
- `POST /` - Crear usuario.
- `GET /{id}/` - Obtener detalle de usuario.
- `PUT /{id}/` - Actualizar usuario completo.
- `PATCH /{id}/` - Actualización parcial de usuario.
- `DELETE /{id}/` - Eliminar usuario.

### Marcas (`/api/marcas/`)
- `GET /` - Listar marcas.
- `POST /` - Crear marca.
- `GET /{id}/` - Obtener detalle de marca.
- `PUT /{id}/` - Actualizar marca completa.
- `PATCH /{id}/` - Actualización parcial de marca.
- `DELETE /{id}/` - Eliminar marca.

### Categorías (`/api/categorias/`)
- `GET /` - Listar categorías.
- `POST /` - Crear categoría.
- `GET /{id}/` - Obtener detalle de categoría.
- `PUT /{id}/` - Actualizar categoría completa.
- `PATCH /{id}/` - Actualización parcial de categoría.
- `DELETE /{id}/` - Eliminar categoría.

### Motocicletas (`/api/motocicletas/`)
- `GET /` - Listar motocicletas.
- `POST /` - Crear motocicleta.
- `GET /{id}/` - Obtener detalle de motocicleta.
- `PUT /{id}/` - Actualizar motocicleta completa.
- `PATCH /{id}/` - Actualización parcial de motocicleta.
- `DELETE /{id}/` - Eliminar motocicleta.

### Cascos (`/api/cascos/`)
- `GET /` - Listar cascos.
- `POST /` - Crear casco.
- `GET /{id}/` - Obtener detalle de casco.
- `PUT /{id}/` - Actualizar casco completo.
- `PATCH /{id}/` - Actualización parcial de casco.
- `DELETE /{id}/` - Eliminar casco.

### Accesorios (`/api/accesorios/`)
- `GET /` - Listar accesorios.
- `POST /` - Crear accesorio.
- `GET /{id}/` - Obtener detalle de accesorio.
- `PUT /{id}/` - Actualizar accesorio completo.
- `PATCH /{id}/` - Actualización parcial de accesorio.
- `DELETE /{id}/` - Eliminar accesorio.

### Pedidos (`/api/pedidos/`)
- `GET /` - Listar pedidos.
- `POST /` - Crear pedido.
- `GET /{id}/` - Obtener detalle de pedido.
- `PUT /{id}/` - Actualizar pedido completo.
- `PATCH /{id}/` - Actualización parcial de pedido.
- `DELETE /{id}/` - Eliminar pedido.

### Pagos (`/api/pagos/`)
- `GET /` - Listar pagos.
- `POST /` - Crear pago.
- `GET /{id}/` - Obtener detalle de pago.
- `PUT /{id}/` - Actualizar pago completo.
- `PATCH /{id}/` - Actualización parcial de pago.
- `DELETE /{id}/` - Eliminar pago.

### Testings (`/api/testings/`)
- `GET /` - Listar pruebas de manejo.
- `POST /` - Crear prueba de manejo.
- `GET /{id}/` - Obtener detalle de prueba de manejo.
- `PUT /{id}/` - Actualizar prueba de manejo completa.
- `PATCH /{id}/` - Actualización parcial de prueba de manejo.
- `DELETE /{id}/` - Eliminar prueba de manejo.

### Otros
- `GET /api/health/` - Verificar estado de la API.
