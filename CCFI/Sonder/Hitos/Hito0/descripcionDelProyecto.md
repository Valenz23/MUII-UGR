# Descripción del proyecto

## Problema

No pasa algunas veces que te acuerdas de una letra de una canción que te gustaba y no te acuerdas del artista. Puedes intentar usar aplicaciones tipo Shazam pero el resultado dependerá de varios factores: lo bien que cantes o si se parecen las letras a las originales. Teniendo mucha suerte puedes encontrarla pero ese es un caso muy improvable.

Entonces, gracias a las características de la aplicación se pueden hacer búsquedas por:
- **Relevancia:** búsquedas ordenadas por la relevancia de la frase que se busque, o parte de ella.
- **Rating:** búsquedas ordenadas por el rating de la frase que se busque, o parte de ella.

En este caso se puede tener más probabilidad de éxito solo si los datos aportados por el usuario son correctos, es decir, si escribe bien la parte de la canción que se acuerda.

## Lógica de negocio

Para crear la solución al problema hay que crear una base de datos con una colección de canciones con sus letras y un rating asociado.

Y como se ha comentado en la sección anterior, las búsquedas se pueden realizar sobre cualquiera de los campos, es decir, autor o autores, tiulo de la canción, o como en el caso expuesto, parte de la letra de la canción.

## Referencias

- La base de datos a usar por el momento será [esta](https://www.kaggle.com/datasets/suraj520/music-dataset-song-information-and-lyrics/data). Contiene nombres de autor, título y letra de canción, y rating. Cuenta con un total de 660 canciones.
- Me he inspirado en el funcionamiento de [esta web](http://www.mldb.org/search?mq=dragon&si=3&mm=1&ob=2).

[Volver](README.md)
