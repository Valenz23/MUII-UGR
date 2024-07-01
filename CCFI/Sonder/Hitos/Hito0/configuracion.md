
# Configuración

En esta sección hablaré del entorno de trabajo que usaré y de la configuración básica de github.

## Entorno de trabajo

+ **Sistema opertativo**: Windows 11.
+ **Editor de código**: VSCode.
		
## Configuracion de GitHub
	
Para el proyecto se va a usar el entorno grafico de github para windows.

Una vez descargado e instalado hay que loguearse. Para ello, en la aplicación hay que dirigirse a la barra superior y a la opción: 

``File -> Options``

y seleccionar el botón **'Sign in'** que esta indicado en la siguiente imagen. 

![foto1](imagenes/foto1.png)


Una vez pulsado ese botón se abrirá una ventana que nos mandara a loguearnos via web.

![foto2](imagenes/foto2.png)


 Nos logueamos y vinculará automáticamente la aplicación con nuestra cuenta de github. (Se sobreentiende que ya tienes una cuenta creada previamente).
 
![foto3](imagenes/foto3.png)

### Clave SSH


Para generar las claves ssh, usaremos la aplicación git-bash. 

En la consola tenemos que escribir:	``ssh-keygen -t ed25519 -C "valenbetis@gmail.com"`` para generar la clave. 

![foto4](imagenes/foto4.png)


Nos preguntara donde queremos guardarlo y una contraseña, en mi caso lo deje en blanco para que lo guarde en el lugar por defecto que se encuentra en el directorio: ``<miUsuario>/.ssh/id_ed25519.pub``.		
		
Para subir la clave a github hay que volver a la web e ir a la sección ``Settings --> SSH and GPG keys``.

![foto5](imagenes/foto5.png) 


Y la añadimos pulsando en el botón indicado en la imagen anterior.

![foto6](imagenes/foto6.png)


Podemos ver en la pagina siguiente como ya tenemos disponible nuestra clave SSH. 

![foto7](imagenes/foto7.png)


Y por ultimo, configuramos nuestra cuenta como nos dice la explicación del hito 0. Poniendo un avatar, nuestro nombre completo, ciudad y universidad.

![foto8](imagenes/foto8.png)	

[Volver](README.md)

