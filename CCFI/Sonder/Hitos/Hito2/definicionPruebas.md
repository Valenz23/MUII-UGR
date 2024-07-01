# Definición de pruebas

Las pruebas tienen que ir en relación con la lógica del negocio propuesta en hitos anteriores.

Recordando un poco, nuestro sistema debería permitir a  los usuarios buscar canciones, añadirlas, borrarlas y cargar lotes de ellas entre otras cosas.

Se han definido varios test que cumplan lo anterior.

![tree dir](img/tree_dir.png)

Los **test** estan ubicados en el directorio ``src\tests\`` y hacen lo siguiente:
- *test_buscarCancion.py*: busca una canción a la BBDD ([ver](../../src/tests/test_buscarCancion.py)).
- *test_anadirCancion.py*: añade una canción a la BBDD ([ver](../../src/tests/test_anadirLote.py)).
- *test_borrarCancion.py*: borra una canción a la BBDD ([ver](../../src/tests/test_borrarCancion.py)).
- *test_anadirLote.py*: añade un lote de canciones a la BBDD ([ver](../../src/tests/test_anadirLote.py)).

Los test realizan las funciones definidas en la clase ``user.py`` ([ver](../../src/clases/user.py)).

El gestor de pruebas se encuetra en el directorio ``src`` en el archivo ``tasks.py`` ([ver](../../src/tasks.py)), y permite realizar todos los test juntos e incluye un comando de ayuda.

Los **comandos** que se observan en la siguiente imagen, y pueden ser obtenidos escribiendo por consola: ``inv ayuda`` o ``invoke ayuda``.

![inv help](img/inv%20help.png)

Realizando todos los test juntos ejecutando el comando ``inv test`` (o invoke) tenemos la siguiente salida.

![inv help](img/inv%20test%20all.png)

Y con esto tenemos los test validados de todas las tareas que hemos definido.

[Volver](README.md)