# Composición del servicio

En total, mi el fichero **[compose.yaml](../../compose.yaml)** consta de cinco contenedores.

A continuación vamos a describir la estructura del fichero, parándonos en cada uno.

**NOTA**: vamos a aprovechar el conocimiento adquirido en las secciones anteriores respecto a los contendores *MySQL* y *ELK*.

## Base de datos

La base de datos esta construida sobre una imagen **MySQL**.

![bd1](img/compose/bd1.png)

Usa el volumen *mysql-data* para guardar los datos.
Para la configuración usa otros dos volumenes que no son compartidos entre los demás servicios:
1. **[init.sql](../../src/BBDD/init.sql)**: Creación y configuración inicial del BBDD.

    ![bd2](img/compose/bd2.png)

2. **[cancionese.csv](../../src/BBDD/canciones2.csv)**: Datos iniciales de la BBDD.

    ![bd3](img/compose/bd3.png)

## API

La API corresponde al contenedor de nuestro proyecto **Sonder**.

![api1](img/compose/api1.png)

Usa el volumen en el que vuelca los logs.

## Logs

Como se ha comentado anteriormente en este hito, para visualizar los logs se usará **ELK**, un paquete que contiene tres contenedores (*elasticsearch*, *logstash* y *kibana*).

Se utilizará **kibana** para visualizar los logs, mientras que con **logstash** configuraremos el fichero de su lectura.

![logs1](img/compose/logs1.png)

El servicio **logstash** usa dos volúmenes:

1. El archivo de configuración **[logstash.conf](../../logstash-config/logstash.conf)**: Donde se define el fichero de logs y el índice que se usará en la visualización.

    ![logs2](img/compose/logs2.png)

2. Volumen correspondiente a los logs.

## Volúmenes

Por último, el fichero comparte los siguientes dos volúmenes entre los servicios.

![vol](img/compose/vol.png)

[Volver](README.md)