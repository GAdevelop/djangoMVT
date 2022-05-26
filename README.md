# djangoMVT: Pasos para el primer entregable en Django. (no es el proyecto final)
Para ingresar al contenido en principio debemos levantar el servidor, escribiendo "python3 manage.py runserver" en la consola.
Una vez que el servidor este activo y funcionando, nos dirigimos al navegador web e introducimos el siguiente URL link: 
http://127.0.0.1:8000/usuarios/familia
Esto nos mostrará la tabla que creamos en models.py, en la cual insertamos data desde views.py y migramos a la base de datos en SQL; no sin primero unir las views al urls.py para que se muestre la información.
Finalmente nos creamos un template para dicha tabla en la cual, con los datos ya ingresados, le damos forma en el archivo .html que nos creamos (en este caso: lista_familiares.html).
