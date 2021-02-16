# Abraxas Task

_En este repositorio encontrán una API Rest desarrollada en Python con el framework Django y Django Rest Framework, así mismo se incluye archvo Dockerfile
para el contendor de la django y Docker-compose para la orquestación de la base de datos en PostgreSQL y la web app en Django._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

_Es necesario tener instalados los siguiente programas para poder tener un entorno de desarrollo y hacer pruebas de forma local_

```
 -Python
 -Docker
 -Docker-compose
```

### Instalación de Docker en Fedora 32/33 🔧

_Para poder realizar la instalación de los Docker en Fedora 32/33 se deberán seguir los siguientes pasos_


```
1. Actualizar los plugins de Fedora con el comando:
     1. sudo dnf -y install dnf-plugins-core
2. Agregar el repositorio de docker al administrador de configuraciones de Fedora.
     1. sudo dnf config-manager \ --add-repo \ https://download.docker.com/linux/fedora/docker-ce.repo
3. Instalando la última versión del motor de Docker:
     1. sudo dnf install docker-ce docker-ce-cli containerd.io_
```

_Comprobamos que se haya instalado correctamente Docker con los siguientes comandos_

```
1. Iniciar el demonio de Docker con el comando:
     1. sudo systemctl start docker
2. Verificamos que el motor de docker se haya instalado correctamente:
     1. sudo docker run hello-world
```

_Si la instalación fue correcta nos debe aparecer la siguiente leyenda:_

```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
$ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
https://hub.docker.com/

For more examples and ideas, visit:
https://docs.docker.com/get-started/
```

_Instalación de Docker-Compose_

_Para realizar la instalación de docker-compose, ya debemos de tener instalado Python, debido a que se utiliza el gestor de paquetes Pip, y Docker Engine._

_Ejecutamos el siguiente comando para poder realizar la instalación de docker-compose._

```
  sudo pip install docker-compose
```

## Ejecutando el contendor con docker-compose ⚙️

_Para ejecutar nos dirigimos en la terminal al path en donde se encuentra nuestro proyecto y ejecutamos los siguientes pasos:_

```
  1. docker-compose build
```

_Este comando nos construirá los contenedores que se especificaron en el archivo docker-compose.yml, esperamos a que se termine de ejecutar el comando._

_Una vez que se terminó de construir nuestro contenedor, procedemos a ejecutar el siguiente comando:_

```
  2. docker-compose up
```

_Este comando nos ayuda a levantar los contenedores, crea la conexión de red, la base de datos y ejecuta los comandos especificados en el apartado *command*.

### Analice las pruebas funcionales 🔩

_Estas pruebas nos proporcionan el buen uso de los endpoints creados para el manejo de las consultas en el proyecto_
_Se realizan pruebas para las diferentes consultas GET, POST, PUT, PATCH, DELETE_

## Construido con 🛠️

* [Django](https://docs.djangoproject.com/) - El framework web usado
* [Django Rest Framework](https://www.django-rest-framework.org/) - Contrucción de API's

## Autor ✒️

* **Eduardo Agreda López** - *Trabajo Inicial* - [eduardoagreda](https://github.com/eduardoagreda)
