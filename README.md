# Info de la materia: ST0263-1716
#### Estudiante(s): Juan Andres Vera, javeraa@eafit.edu.co - Samuel Garcia Correa, sgarciac6@eafit.edu.co

#### Profesor: ALVARO ENRIQUE OSPINA SANJUAN , aeospinas@eafit.brightspace.com

## Sistema P2P para Compartición de Archivos
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
### Comunicación REST (Flask):
- Se ha implementado un servidor Flask (server.py) que actúa como la interfaz REST para el sistema P2P.
- Se ha implementado un servicio gRPC Pclient y Pserver, que aprovechan la comunicación gRPC para coordinar las operaciones entre nodos.
- Sistema P2P
- despliegue en docker

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
- Despliegue en AWS
- Manejo de algunos errores
## 2. Información General de Diseño de Alto Nivel
### Arquitectura
El proyecto implementa una red P2P descentralizada donde cada nodo actúa tanto como cliente como servidor. Los nodos intercambian información utilizando microservicios que implementan diferentes patrones de comunicación, tales como API REST, gRPC, y MOM (Message Oriented Middleware).

### Patrones y Mejores Prácticas Utilizadas
#### Microservicios:
 Cada funcionalidad del sistema está desacoplada en diferentes microservicios, lo que facilita la escalabilidad y el mantenimiento.

#### Concurrencia:
 Los microservicios soportan la concurrencia, permitiendo que múltiples solicitudes sean manejadas simultáneamente.

#### RPC (Remote Procedure Call):
 Utilizado para la comunicación entre nodos mediante gRPC, permitiendo llamadas a procedimientos remotos de manera eficiente.

#### API REST:
 Arquitectura RESTful para la comunicación entre procesos utilizando HTTP.

#### MOM (Message Oriented Middleware): 
Utilizado para la comunicación asíncrona entre nodos a través de colas de mensajes.

## 3. Descripción del Ambiente de Desarrollo y Técnico

Lenguaje de Programación y Librerías
Lenguaje: Python 3.8+

#### Librerías y Paquetes:
grpcio==1.39.0: Implementación de gRPC para Python.
protobuf==3.17.3: Serialización de datos para gRPC.
Flask==2.0.1: Microframework para la implementación de API REST.
pika==1.2.0: Cliente de Python para AMQP (Advanced Message Queuing Protocol).

#### Ambiente de Desarrollo
Sistema Operativo: Ubuntu 20.04 o superior
Herramientas: Docker (para contenedores), Git (para control de versiones)

#### Compilación y Ejecución
#### Clonar el Repositorio:
> git clone <https://github.com/Vera3588/javeraa--st0263.git>
> cd javeraa--st0263-main

#### Construir el Contenedor Docker:

> docker build -t taller1 .

#### Ejecutar el Contenedor:

> docker run -d -p 50051:50051 taller1

## 4. Detalles del Desarrollo
#### Detalles Técnicos

El proyecto está dividido en varios microservicios que manejan diferentes aspectos del sistema P2P. La comunicación entre nodos se realiza utilizando REST, gRPC, y MOM. Cada nodo puede listar los archivos disponibles en un directorio específico y compartir el índice de estos archivos con otros nodos.

#### Configuración del Proyecto
Archivo de Configuración: Cada nodo tiene un archivo de configuración que especifica:
IP y Puerto: Dirección y puerto en el que el nodo escucha las solicitudes.
Directorio de Archivos: Directorio en el que el nodo busca archivos para compartir.
Peer Semilla: URL de un nodo semilla para unirse a la red.

archivo de configuración (config/peer_config.json):
{
    "ip": "0.0.0.0",
    "port": 5000,
    "directory": "/path/to/shared/files",
    "seed_peer": "http://peer2.example.com"
}


#### Estructura de Directorios y Archivos Importantes

![image](https://github.com/user-attachments/assets/f2ba564e-8353-4bc4-afa9-1f86facb2a43)


## 5. Descripción del Ambiente de Ejecución

Lenguaje de Programación y Librerías en Producción
Lenguaje: Python 3.8+
Librerías y Paquetes: (Las mismas que en desarrollo)

#### IP o Nombres de Dominio
Los nodos pueden ejecutarse en cualquier máquina con una IP pública o privada. Se pueden configurar IPs específicas o usar nombres de dominio si se despliega en la nube.

#### Configuración de Parámetros
Los parámetros de configuración se manejan mediante el archivo config/peer_config.json. Es importante configurar correctamente la IP, el puerto y el directorio de archivos.

#### Lanzamiento del Servidor
Para iniciar un nodo:
python3 services/pserver.py --config config/peer_config.json

#### Guía de Uso
Iniciar un Nodo: Configura el archivo peer_config.json y lanza el servidor.
Buscar Archivos: Utiliza el cliente (pclient.py) para consultar otros nodos sobre archivos disponibles.
Compartir Archivos: Los nodos automáticamente comparten el índice de sus archivos con otros nodos en la red.

## 6. Referencias
- gRPC Official Documentation
- Flask Documentation
- Pika Documentation
- https://www.youtube.com/watch?v=psYAhc9JUyo

