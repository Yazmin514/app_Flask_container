# basic_flaskapp_container
# Base de datos Distribuidos
En la materia de Bases de Datos distribuidas se realizo una practica donde se utilizo el lenguaje de programacion de Python con flask y para la base de datos mongodb.
# Herramientas
1.-Para la ejecucion del proyecto necesitaremos un editor de texto

2.-Un navegador

3.-Una terminal para la ejecucion del proyecto
# Intrucciones y Comandos 
1.-Clonar el repositorio

2.-Compilar el contenedor dentro de la terminal

 -cd basic_flaskapp_container
 
 -sudo docker-compose up -d
 
3.-Verificar que los contenedores esten corriendo:

  -sudo docker ps
  
4.-Entrar a la direccion desde el navegador para ver la aplicacion Flask funcionando:

  -http://localhost:8181
  
5.-Para detener docker desde la terminal es el siguiente comando:

  ctr+c

6.-Para verificar los datos de las personas que han sido registradas en la base de datos en mongo se utilizan estos comandos:
 
  verificar el id de mongo: 
  
  -sudo docker ps
  
  -sudo docker exec -t (se coloca el id_mongo) bash
  
  -mongo --version
  
  -mongo
  
  -shows dbs
  
  -use testdb
  
  -show collections
  
  -db.post.find()

7.-Para eliminar los datos ingresados a la base de datos es:

 -db.post.drop()
  
  
 
 
