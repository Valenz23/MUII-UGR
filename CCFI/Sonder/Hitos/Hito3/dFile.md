# Dockerfile

EL documento [Dockerfile](../../Dockerfile) está dividido en varias secciones:

1. Seleccionamos el contenedor base e instalamos sobre él los paquetes de `python`, `pip` y `bash`.

    ![Parte 1 Dockerfile](img/docker_1.png)

2. Creaamos el entorno virtual necesario para usar `invoke`.

    ![Parte 2 Dockerfile](img/docker_2.png)

3. Copiamos todo el código de nuestro proyecto y, seleccionamos el fichero donde se trabajará y se ejecutarán los test.

    ![Parte 3 Dockerfile](img/docker_3.png)

4. Y por último, mandamos la orden para que se ejecuten los test.

    ![Parte 4 Dockerfile](img/docker_4.png)

### Ejecutando Dockerfile

Desde consola podemos ejecutar la siguiente orden: `"docker build -t sonder ."`, para así construir la imagen de nuestro proyecto.

![Cosntruir imagen](img/exec1.png)

Como hemos usado un contenedor muy ligero, después de ejecutar el documento `Dockerfile` obtenemos una imagen que apenas pesa unos 100 MB, como se puede observar en las siguientes figuras.

![ver imagen 1](img/comp1.1.png)
![ver imagen 2](img/comp1.png)

Para probar el contenedor y ver si pasa los test nos dirigimos una vez más a la consola de comandos y escribimos `docker run --name sonder sonder`.

![Ejecutar contenedor](img/comp2.png)

Vemos que pasa los test, por lo que ya tendriamos un contenedor que funciona correctamente. El próximo paso será publicar nuestro contenedor en **Docker Hub** y otro servicio de contenedores como **GitHub Packages**.

[Volver](README.md)