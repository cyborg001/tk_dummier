# tk_dummier
# programa que genera el comentario de un evento sismico y lo publica en la pagina del sismologico
# este programa fue creado el creado el 13-10-2018
# por carlos ramirez
#
#
#
# El programa necesita los siguientes archivos para su correcto funcionamiento.
# 1-funciones-sismicas.py, funciones necesarias creada para el programa.
# 2-localidades_2mundo.dat,aqui estan las locaciones de las ciudades del pais y algunas regiones cercanas.
# 3-hyp.out, entrada generada por el automatico con los datos brutos llegados de las estaciones.
# 4-contactos.txt,donde estan todos los correos electronicos de los contactos pertinentes. Uno por linea.
# 5-contactos_sini.txt, donde estan todos los contactos del sini.
# 6-paths.txt, donde se configuran las direcciones de los archios a leer(hyp.out),de salida(dummyX.dat) y dummyX.copy.
# 7-provinciascsv, donde estan todos los poligonos de las provincias y regiones cercanas al pais.

El archivo path.txt posee tres lineas, la primera linea es la direccion donde esta el hyp.out, la segunda linea es
la direccion para donde va el dummyX.dat el cual lee el servidor web y la ultima linea es la direccion donde
va el dummyX.copy que es una especie de catalogo o base de datos de los archivos generados por el tk_dummier o el 
tk_hyper


