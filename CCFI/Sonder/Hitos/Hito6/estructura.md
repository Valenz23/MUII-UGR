# Definción de la estructura de contenedores

La estructura definida para completar este hito debe constar de al menos 3 contenedores. Uno de ellos contendrá nuestra API y los demás alojaran la base de datos y el servidor de logs.

A continuación explicaré varias opciones que tenemos para elegir en cuestión de contenedores para bases de datos y logs.

## Bases de datos

Existen diversas opciones de contenedores para bases de datos que ofrecen  flexibilidad y eficiencia en el despliegue de estos sistemas. Se han popularizado la adopción de contenedores de bases de datos ya que permiten la encapsulación de la BBDD y sus dependencias en un entorno aislado. Entre algunas opciones se encuentran *MySQL*, *PostgreSQL*, *MongoDB*, etc, cada una ofreciendo características específicas y adaptadas a diferentes necesidades. Estos contenedores, como ya he comentado, permite desplegar fácilmente entornos de bases de datos, gestionar versiones, facilitando el desarrollo, pruebas y despligue de APIs dependientes de sistemas de gestión de bases de datos.

Como puedo elegir libremente al estar creando la base de datos desde cero, el contenedor que usaré es el de **MySQL**.

## Logs

Una opción popular para visualizar logs desde el navegador es *Elacticsearch*. Esta herramienta forma parte de **ELK** (*Elasticsearch*, *Logstash* y *Kibana*) y son ampliamente utilizadas para recopilar, almacenar y visualzizar logs.

Esta opción nos obliga a usar tres contenedores adicionales. Mediante **Logstash** leeremos los datos del fichero de log, y con **Kibana** podremos visualizarlos vía web.

## Estructura final de contenedores

La estructura de contenedores definida para mi proyecto es la siguiente:

* **API**: Sonder
* **BBDD**: MySQL
* **Logs**: ELK

La orquestación esta documentada en su sección correspondiente.

[Volver](README.md)