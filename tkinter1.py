# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 11:50:37 2017

@author: Cgrs scripts
"""


import sys
import os.path
import funciones_sismicas as fc

PYTHON_VERSION = sys.version_info.major

PYTHON_VERSION

if PYTHON_VERSION < 3:
    try:
        import Tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo Tkinter")
else:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError("se requiere el modulo tkinter")
from tkinter import font

#################################################################################
## esta funcion genera el comentario y lo envia a la pagina, ademas de enviar
## los correos al sini automaticamente y la opcion de enviar correo a las partes
## interesadas.
##
## internaente necesita los archivos paths.txt de donde tomara las direcciones
## paths.txt tiene tres lineas:la primera de donde esta localizado el hyper.out
## la segunda  a donde enviara el dummyX.dat
## y la tercera a donde ira el dummyX.copy
##
## tambien tomara el archivo contactos.txt donde estaran los correos electroni
## cos de las partes interesadas, y contactos_sini.txt donde estaran los corre-
## os que se enviaran automaticamente al sini
##
################################################################################

def crear_hyper():
    paths = open("paths.txt").readlines()
    path_poligonos = 'provinciascsv'
    path_ciudades = 'localidades_2mundo.dat'
    hyp_path = paths[0][:-1]#'hyp.out'#r'Z:\seismo\WOR\hyp.out' 

    fpath = open(hyp_path)
    linea = fpath.readline()
    fpath.close()
    ciudades = fc.get_ciudades(path_ciudades)
    formato = fc.formatear_hyp(linea,path_poligonos,ciudades,mag_var.get())
    salida = paths[1][:-1]#'dummyX.dat'#r'X:\dummyX.dat' 
    fsalida = open(salida,'w')
    fsalida.write(formato[0])
    fsalida.close


    
    
    salida_copy =  paths[2][:-1]#'dummyX.copy'#r'Z:\seismo\WOR\dummyX.copy'
    if os.path.isfile(salida_copy)==False:
        fsalida = open(salida_copy,'w')
        fsalida.close()

    fsalida = open(salida_copy,'r')
    s_salida = fsalida.readlines()
    i_d=[]
    for n in s_salida:
        if len(n)<10:
            s_salida.remove(n);
    for n in s_salida:
        i_d.append(n.split()[0])
    if formato[1] not in i_d:
        s_salida.append(formato[0]+'\n')
    else:
        s_salida[i_d.index(formato[1])] = formato[0]+'\n'
    s_salida = fc.ordenar(s_salida)
    salida =""
    for n in s_salida:
        #print n
        salida+=n
    fsalida.close()


    fsalida = open(salida_copy,'w')
    fsalida.write(salida)
    fsalida.close()
    
    
    
    archivos_sini=open('contactos-sini.txt','r').readlines()
        #contactos_sini=['cramirez27@uasd.edu.do','cgrs27@gmail.com']#,'jleonel78@uasd.edu.do']
        
    contactos_sini=[]
    contactos_sini = [n[:-1] for n in archivos_sini if n not in contactos_sini]
    contactos_sini[-1]=archivos_sini[-1]
        #print(contactos_sini)
    fc.enviarEmail(contactos_sini,formato[3])#si quieres en modo html anadir un tercer
        
        #esta parte envia los correos
        #destinatario =['cramirez27@uasd.edu.do','cgrs27@gmail.com']
        #destinatario =['cramirez27@uasd.edu.do','cgrs27@gmail.com','jleonel78@uasd.edu.do','amoreta78@uasd.edu.do']#,
                   #'sismos@sini.gob.do']
    if(bool_todos.get()):
        #argumento: 'html'
        archivos_contactos=open('contactos.txt','r').readlines()
        #contactos =['cramirez27@uasd.edu.do','cgrs27@gmail.com']#,'jleonel78@uasd.edu.do']
        #print(archivos_contactos[-1])
        contactos=[]
        contactos = [n[:-1] for n in archivos_contactos if n not in contactos]
        
        contactos[-1]=archivos_contactos[-1]
        fc.enviarEmail(contactos,formato[3],'html')


#parte que crea la aplicacion grafica
root = tk.Tk()
root.title('Hyper')
root.geometry('500x240')
root.resizable(width=False, height=False)
font_size = font.Font(weight='bold',size=14)
mag_var = tk.IntVar()
bool_sini = tk.BooleanVar()
bool_todos = tk.BooleanVar()
backcolor='white smoke'
root.configure(background=backcolor)
#font_size=17
rbcoda = tk.Radiobutton(text="Mag Coda       ",background=backcolor,
                        font=font_size,variable=mag_var, value=1)
rblocal = tk.Radiobutton(text="Mag Local       ",background=backcolor,
                         font=font_size, variable=mag_var, value=2)
rbmw = tk.Radiobutton(text="Mag MW         ",background=backcolor,
                      font=font_size, variable=mag_var, value=3)
rbprom = tk.Radiobutton(text="Mag Promedio",background=backcolor,
                        font=font_size, variable=mag_var, value=4)

etiqueta = tk.Label(root,text='')
#ch_correos = tk.Checkbutton(root,text='Enviar correos a sini',variable=bool_sini)
ch_todos = tk.Checkbutton(root,text='Enviar correos a todos',
                          background=backcolor,font=font_size,variable=bool_todos)
etiqueta2 = tk.Label(root,text=' ')
boton = tk.Button(root,text='Enviar Dummy',font=font_size,background='forest green',
                  foreground='yellow',command=crear_hyper)

etiqueta.grid(row=1,column=1)
rbcoda.grid(row=3,column=1)
rblocal.grid(row=2,column=1)
rbmw.grid(row=4,column=1)
rbprom.grid(row=5,column=1)
#ch_correos.grid(row=7,column=1)
ch_todos.grid(row=5,column=2)
etiqueta2.grid(row=8,column=1)
boton.grid(row=9,column=1)


root.mainloop()
