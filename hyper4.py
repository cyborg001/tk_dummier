# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:09:50 2017

@author: carlos
"""
import json
import os.path
import funciones_sismicas as fc
def formatear_hyp(linea,path_poligonos,path_ciudades):
    anio = linea[1:5]
    mes = linea[6:8]
    dia = linea[8:10]
    if mes[0]==' ':
        mes=str(0)+mes[1]
    if dia[0]== ' ':
        dia = str(0)+dia[1]
    h = linea[11:13]
    if h[0]==' ':
        h =  str(0)+h[1]
    m = linea[13:15]
    if m[0]==' ':
        m = str(0)+m[1]
    s = linea[16:18]
    if s[0]==' ':
        s = str(0)+s[1]
    lat = linea[24:30]
    lon = linea[31:38]
    fecha = anio+'-'+mes+'-'+dia
    hora = h+':'+m+':'+s
    i_d = anio+mes+dia+h+m
    deph = linea[38:43]
    l = linea[56:-1]
    ml = ''
    mc = ''
    mw = ''
    mag = ''
    if 'L' in l:
        ml = l[l.index('L')-3:l.index('L')]
    if 'C' in l:
        mc = l[l.index('C')-3:l.index('C')]
    if 'W' in l:
        mw = l[l.index('W')-3:l.index('W')]
    if mc!='':
        mag = mc
    elif ml !='':
        mag = m
    else:
        mag = mw
    '''
    #si cualquier mangnitud es mayor a 3.5 
    if float(ml) > float(mc):
        if float(ml) > float(mw):
            mayor = float(ml)
        else:
            mayor = float(mw)
    else:
        mayor = float(mc)
    if mayor > 3.5:
        salida2 = lat+'  '+lon+'  '+deph+'  '+str(mayor)
    '''    
       
    
    sal=i_d+ '  '+fecha+'  '+hora+'  '+lat+'  '+lon+'  '+deph+'  '+mag+'  '
    comentario = fc.generar_comentario(path_ciudades,float(lat),float(lon),path_poligonos)
    #json = "{'i_d':'"+i_d+"','fecha':'"+fecha+"','hora':'"+hora+"','lat':'"+lat+"','lon':'"+lon+"','deph':'"+deph+"','mag':'"+mag+"','comentario':'"+comentario+"}"
    obj = {"fecha":fecha, "hora":hora, "lat":lat, "lon":lon, "depth":deph, "mag":mag, "comentario":comentario}
    #print (json.dumps(obj))
    return sal + comentario,i_d,sal,obj


path_poligonos = 'provinciascsv'
path_ciudades = 'localidades_2mundo.dat'
hyp_path =r'Z:\seismo\WOR\hyp.out' #'hyp.out'

fpath = open(hyp_path)
linea = fpath.readline()
fpath.close()
ciudades = fc.get_ciudades(path_ciudades)
formato = formatear_hyp(linea,path_poligonos,ciudades)
#print (formato[2])
salida = r'X:\dummyX.dat' #'dummyX.dat'
fsalida = open(salida,'w')
fsalida.write(formato[0])
fsalida.close()
'''
archivos_contactos=open('contactos.txt','r').readlines()
contactos=[]
contactos = [n[:-1] for n in archivos_contactos if n not in contactos]
contactos[-1]=archivos_contactos[-1]
print(contactos)    
archivos_sini=open('contactos-sini.txt','r').readlines()
contactos_sini=[]
contactos_sini = [n[:-1] for n in archivos_sini if n not in contactos_sini]
contactos_sini[-1]=contactos_sini[-1]
'''
#print(contactos_sini)
#esta parte envia los correos
#destinatario =['cramirez27@uasd.edu.do','cgrs27@gmail.com']
#destinatario =['cramirez27@uasd.edu.do','cgrs27@gmail.com','jleonel78@uasd.edu.do','amoreta78@uasd.edu.do']#,
               #'sismos@sini.gob.do']
#fc.enviarEmail(contactos_sini,formato[3])#si quieres en modo html anadir un tercer
#argumento: 'html'
#fc.enviarEmail(contactos,formato[3],'html')
salida_copy =  r'Z:\seismo\WOR\dummyX.copy'#'dummyX.copy'
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
