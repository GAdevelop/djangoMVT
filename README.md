# djangoMVT: Pasos para el proyecto final en Django.


Para ingresar al contenido en principio debemos levantar el servidor, escribiendo "python3 manage.py runserver" en la consola.


Una vez que el servidor este activo y funcionando, nos dirigimos al navegador web e introducimos el siguiente URL link: http://127.0.0.1:8000/usuarios/


Esto nos mostrará la página web creada con todos los archivos html en regla. Para ver la lista de cada modelo en la base de datos, haremos click en los distintos titulos en el encabezado de la página: "Materias", "Profesores", "Estudiantes"; en caso de querer buscar las listas desde el URL, deberemos ingresar a los siguientes links:
http://127.0.0.1:8000/usuarios/materias
http://127.0.0.1:8000/usuarios/profesores
http://127.0.0.1:8000/usuarios/estudiantes
Una vez hecho esto, podremos ver cada lista en una tabla con sus distintos tipos de contenido.


Próximamente, nos dirigimos al siguiente URL link para intentar agregar información a una tabla (en este caso la tabla de estudiantes): http://127.0.0.1:8000/usuarios/formulario_estudiantes
Desde aqui podremos ingresar los tres parámetros requeridos obligatoriamente para insertar la información en la base de datos y su vez, en la tabla.


Una vez hecho esto podemos chequear que la información haya sido ingresada, apretando nuevamente el titulo de "Estudiantes" en el encabezado.


Finalmente nos movemos al último URL para poder buscar información sobre dicha tabla pasando cualquiera de los tres parámetros previamente requeridos: http://127.0.0.1:8000/usuarios/buscar_estudiantes