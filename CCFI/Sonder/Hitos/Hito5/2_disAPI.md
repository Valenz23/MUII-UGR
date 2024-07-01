# Diseño de la API

La API implementará las funciones que hemos desarrollado en los hitos anteriores siguiendo la lógica de nuestro problema. Además, se han incluido **dos nuevas funciones** de acuerdo a las historias de usuario **HU2** y **HU3**, que permiten listar canciones por popularidad y modificar la letra de una canción.

## Rutas generadas

La API se encuentra en esta dirección: [API](../../src/api/sonder_api.py)

Y las rutas generadas son las siguientes:
- **/status**: Comprueba si la API está funcionando.
- **/buscar**: busca una canción por los siguientes parámetros:
    - *atributo*: puede ser *artista*, *titulo* y *letra*.
    - *valor*: el valor del atributo.
- **/add**: añade una canción. Hay que proporcionar los siguientes parámetros:
    - *artista*: nombre del artista/grupo.
    - *titulo*: nombre de la canción.
    - *letra*: letra de la canción.
- **/del**: borra la canción con la que corresponda el parámetro *id*.
- **/lote**: añade canciones en lote, dada la ruta (*path*) de ese lote.
- **/lista**: Lista las canciones ordenadas por popularidad. Implementa la historia de usuario **HU2**.
- **/mod**: Modifica la letra de la canción correspondiente a un id dado. Implementa la historia de usuario **HU3** y necesita estos parámetros:
    - *id*: identificador de la canción en la BBDD.
    - *letra*: letra corregida de la canción.

Para realización de estas funcionalidades ha sido necesario usar los métodos **GET**, **PUT** y **DELETE**. Si probamos a pasar los tests obtenemos la imagen siguiente (si todo ha ido bien).

![tests](img/tests.png)

Las pruebas de la API se verán en su sección correspondiente de este hito.

[Volver](README.md)
