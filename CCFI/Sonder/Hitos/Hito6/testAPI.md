## Prueba de la API y visualización de logs

Para finalizar el hito, vamos a realizar una bateria de pruebas sobre la API y mostraremos la salida que obtenemos finalizando con una visualización de los logs.

**NOTA**: Para poder ver los logs la primera vez que nos dirijamos a la dirección ``localhost:5601``, tenemos que seguir los mismos pasos que los expuestos en este [documento](confELK.md#ejecución-y-test) de este hito. Esto sólo es necesario hacerlo la primera vez.

## Batería de test

La siguiente batería de test se ha hecho siguiendo el mismo orden de la lista, entre la hora **12:00** y **12:06** del 4 de Febrero de 2024.

1. **Búsqueda del artista test**: no hay datos.

    ![test1](img/tests/test1.png)

2. **Inserción del artista test**.

    ![test2](img/tests/test2.png)

3. **Búsqueda otra vez del artista: test**: aparecen los datos que acabamos de insertar.

    ![test3](img/tests/test3.png)

4. **Modificación de la letra de la canción con id=1111**.
    ![test4](img/tests/test4.png)

5. **Búsqueda del artista test**: comprobación de que la letra se ha modificado.

    ![test5](img/tests/test5.png)

6. **Borrado de la canción con id=1111**.

    ![test6](img/tests/test6.png)

7. **Búsqueda del artista test**: comprobación del borrado de la canción.

    ![test7](img/tests/test7.png)

8. **Listado de canciones por popularidad**.

    ![test8](img/tests/test8.png)

9. **Inserción de lote de canciones**.

    ![test9](img/tests/test9.png)

8. **Listado de canciones por popularidad**: comprobamos que las nuevas canciones insertadas aparecen en el listado.

    ![test10](img/tests/test10.png)


## Visualización de logs

Ahora vamos a comprobar si se actualizan los logs con estas llamadas.

![vis1](img/tests/vis1.png)

![vis2](img/tests/vis2.png)

Como se puede ver en las imágenes anteriores, las fechas (señaladas en rojo) coinciden con la hora a la que realizaron las llamadas a la API, es decir, somos capaces de visualizar los logs correctamente.

[Volver](README.md)