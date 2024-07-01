# Cambios en la API

El fichero de llamadas a la **[API](../../src/api/sonder_api.py)**, ha sufrido un gran cambio respecto al hito 5. Se ha tenido que adaptar todo el código para que se conecte a la base de datos que vamos a usar, y todas las llamadas son consultas sobre esa base de datos.

## Llamadas a la API

* **Conexión a la base de datos**:

    ![api1](img/api/api1.png)

* **Buscar**:

    ![api2](img/api/api2.png)

* **Insertar**:

    ![api3](img/api/api3.png)

* **Borrar**:

    ![api4](img/api/api4.png)

* **Insertar lote**:

    ![api5](img/api/api5.png)

* **Listar por popularidad**:

    ![api6](img/api/api6.png)

* **Modificar letra**:

    ![api7](img/api/api7.png)

## Test y Logs

Los **[test](../../src/api/test_sonder_api.py)** sobre la API en este hito no han variado, y el resultado de los **logs** son los que se pueden ver en la siguiente imagen:

![api8](img/api/api8.png)


[Volver](README.md)