# Configuración de ELK



## Prueba del compose

Para probar el funcionamiento de ELK necesitamos los tres contenedores correspondientes, por lo que tenemos que montar el fichero ``compose.yaml`` con estos servicios.

![test1](img/elk/test1.png)

En el fichero anterior, usamos los servicios de elasticsearch y kibana, con sus puertos correpondiente. En el servicio de logstash hay un poco más de detalle, se usan dos volúmenes para copiar archivos en "local" al cotenedor.

Los archivos contienen:
1. **Un archivo de configuración**: 

![test2](img/elk/test2.png)

2. **El fichero de logs**: Con el mismo formato visto en hitos anteriores.

![test3](img/elk/test3.png)

## Ejecución y test

Ejecutamos la orden ``docker compose up``.

![test4](img/elk/test4.png)

Una vez tengamos los servicios activos, nos dirigimos a nuestro navegador a la dirección ``localhost:5601``, correspondiente a **Kibana**.

Seguido, nos dirigimos a la ``Management > Index Patterns`` , y añadimos el índice que hemos nombrado en el fichero de configuración de **Logstash** (en este caso, logs).

Ahora nos dirigimos al menu lateral izquierdo y seleccionamos ``Discover`` como se muestra en la figura siguiente:

![test5](img/elk/test5.png)

Y como se puede observar en la siguiente imagen, se han cargado los **logs** del fichero y ya son accesibles vía web.

![test6](img/elk/test6.png)

Como en el apartado anterior, este estudio realizado hay que aplicarlo ahora en nuestra API.

[Volver](README.md)