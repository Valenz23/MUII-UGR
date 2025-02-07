# Práctica 3: Desarrollo de una Aplicación Android para Comercio Electrónico

## Descripción General
Esta aplicación Android se ha diseñado como un cliente para un sistema de comercio electrónico, ofreciendo las siguientes funcionalidades principales:

- Consulta y visualización de un catálogo de productos.
- Administración de un carrito de compras.
- Realización de pedidos y gestión de productos para usuarios autorizados.
- Visualización de ubicaciones mediante Google Maps.

Este proyecto forma parte del aprendizaje y práctica de integración con APIs RESTful, así como el uso de herramientas avanzadas en Android Studio.

## Requisitos de Instalación y Ejecución

### Requisitos Previos
- Instalar Android Studio con el JDK integrado (jbr-21).
- Configurar un dispositivo físico o emulador compatible para realizar pruebas.
- Configurar la API con Spring Boot para poder ejecutar el backend.

### Pasos para la Instalación
1. Descargar el proyecto
2. Abrirlo en Android Studio.
3. Sincronizar las dependencias de Gradle cuando el IDE lo solicite.

## Dependencias Utilizadas

- **Retrofit:** Biblioteca para la gestión de peticiones HTTP y consumo de la API REST.
- **Gson:** Utilizada para la serialización y deserialización de datos en formato JSON.
- **Google Maps API:** Integrada para ofrecer funcionalidad de mapas y localización.

## Organización del Proyecto

El código está estructurado para facilitar la navegación y el mantenimiento. La organización de carpetas es la siguiente:

```
├── src/
│   ├── androidTest/                # Pruebas específicas para Android
│   ├── main/
│       ├── java/
│           ├── com/example/practica3/
│               ├── api/            # Interfaces y controladores para la API REST
│               ├── ui/             # Actividades de la aplicación
│               ├── AddProductActivity
│               ├── CartActivity
│               ├── EditProductActivity
│               ├── LoginActivity
│               ├── MainActivity
│               ├── MapActivity
│               ├── ThankYouActivity
│       ├── res/                    # Recursos visuales
│       ├── AndroidManifest.xml     # Configuración del proyecto
```

## Endpoints RESTful:
- **Productos:**
  - `GET /api/productos`: Obtiene la lista de productos.
  - `POST /api/productos/add`: Añade un nuevo producto.
  - `PUT /api/productos/update/{id}`: Actualiza un producto existente.
  - `DELETE /api/productos/delete/{id}`: Elimina un producto mediante su ID.
- **Carrito:**
  - `GET /api/carrito`: Recupera el contenido del carrito.
  - `POST /api/carrito/add`: Agrega un producto al carrito.
  - `POST /api/carrito/clear`: Vacía el carrito.
  - `POST /api/carrito/comprar`: Realiza la compra.
- **Login:**
  - `POST /api/login`: Realiza la autenticación de un usuario.