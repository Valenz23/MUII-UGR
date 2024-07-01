import hug # desde .. huf -f api/sonder_api.py
import logging

# from clases.user import * 
# from clases.cancion import *

import mysql.connector
import csv

# configuracion de logging
logging.basicConfig(filename='./logs/app.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)

def conectarDB():
    conf = {
        'host': 'mysql',
        'user': 'myuser',
        'password': 'secret',
        'database': 'sonder'
    }
    conexion = mysql.connector.connect(**conf)
    return conexion

# se prueba si la conexion a la base de datos es correcta
@hug.get('/status')
def status():

    mensaje = ''

    try:     
        conexion_db = conectarDB()
        sql = "CREATE TABLE IF NOT EXISTS cancion (id INT PRIMARY KEY, artista VARCHAR(255), titulo VARCHAR(255), letra TEXT, popularidad DECIMAL(5, 2))";        
        with conexion_db.cursor() as cursor:
            cursor.execute(sql)
        conexion_db.commit()          
        mensaje = "Conexión a la base de datos establecida."    
        logging.info(mensaje)
        status = "OK"
    except mysql.connector.Error as err:
        mensaje = f"Error de conexión a la base de datos: {err}."    
        logging.error(mensaje)
        status = "Error"

    return { 
		"mensaje":mensaje,
		"status":status
    }

@hug.get('/buscar')
def api_buscar_cancion(atributo: str, valor: str):

    sql = f'SELECT * FROM cancion WHERE {atributo} LIKE "%{valor}%"'
    mensaje = ''
    status = ''
    resultado = ''

    try:
        conexion_db = conectarDB()
        with conexion_db.cursor() as cursor:                        
            cursor.execute(sql)
            resultado = cursor.fetchall()
            mensaje = 'Consulta: {} | Resultado: {}'.format(sql,resultado)
        status = "OK"
        logging.info(mensaje)

    except Exception as e:
        mensaje = f'Error en la consulta: {str(e)}'
        resultado = None
        status = "Error"
        logging.error(mensaje)

    return {
        "mensaje": mensaje,
        "resultado": resultado,
        "status": status
    }


@hug.put('/add')
def api_add_cancion(id:int, artista:str, titulo:str, letra:str):

    sql = f'INSERT INTO cancion (id, artista, titulo, letra, popularidad) VALUES ("{id}", "{artista}", "{titulo}", "{letra}", 0)'    
    mensaje = ''
    status = ''

    try:
        conexion_db = conectarDB()
        with conexion_db.cursor() as cursor:
            cursor.execute(sql)
        conexion_db.commit()        
        mensaje = f'Insertar cancion: {sql}'
        status = 'OK'
        logging.info(mensaje)
    except Exception as e:
        mensaje = f'Error al insertar: {str:(e)}'
        status = 'Error'
        logging.error(mensaje)
    
    return {
		  "mensaje":mensaje,
		  "status":status
    }

@hug.delete('/del')
def api_delete_cancion(id:int):

    sql = f'DELETE FROM cancion WHERE id={id}'
    mensaje = ''
    status = ''

    try:
        conexion_db = conectarDB()
        with conexion_db.cursor() as cursor:
            cursor.execute(sql)
        conexion_db.commit()
        mensaje = f'Borrar cancion: {sql}'
        status = 'OK'
        logging.info(mensaje)
    except Exception as e:
        mensaje = f'Error al borrar: {str:(e)}'
        status = 'Error'
        logging.error(mensaje)

    return {
		  "mensaje":mensaje,
		  "status":status
    }

@hug.put('/lote')
def api_add_lote(path:str):

    sql = ''
    mensaje = ''
    status = ''

    try:     
        archivoCSV = path
        conexion_db = conectarDB()
        with open(archivoCSV, 'r') as archivo:
            lector = csv.reader(archivo)
            next(lector,None)
            cursor = conexion_db.cursor()
            mensaje = f'Insertar lote: {path}'

            for fila in lector:
                id, artista, titulo, letra, popularidad = fila
                sql = f'INSERT INTO cancion (id, artista, titulo, letra, popularidad) VALUES ("{id}", "{artista}", "{titulo}", "{letra}", "{popularidad}")'    
                mensaje += f' && {sql}'
                cursor.execute(sql)  
        
        
        conexion_db.commit()
        status = 'OK'
        logging.info(mensaje)
    except Exception as e:
        mensaje = f'Error al insertar: {str:(e)}'
        status = 'Error'
        logging.error(mensaje)

    return {
		  "mensaje":mensaje,
		  "status":status
    }  

@hug.get('/lista')
def api_listar_canciones():

    sql = f'SELECT * FROM cancion ORDER BY popularidad DESC LIMIT 5'
    mensaje = ''
    status = ''
    resultado = ''

    try:
        conexion_db = conectarDB()
        with conexion_db.cursor() as cursor:            
            cursor.execute(sql)
            resultado = cursor.fetchall()
        mensaje = 'Listar por popularidad: {} | Resultado: {}'.format(sql, resultado)
        status = "OK"
        logging.info(mensaje)

    except Exception as e:
        mensaje = f'Error en el listado: {str(e)}'
        resultado = None
        status = "Error"
        logging.error(mensaje)

    return {
        "mensaje": mensaje,
        "resultado": resultado,
        "status": status
    }

@hug.put('/mod')
def api_modificar_letra(id:int, letra:str):

    sql = f'UPDATE cancion SET letra="{letra}" WHERE id={id}'
    mensaje = ''
    status = ''

    try:
        conexion_db = conectarDB()
        with conexion_db.cursor() as cursor:
            mensaje = f'Modificando letra: {sql}'
            cursor.execute(sql)
        conexion_db.commit()
        status = 'OK'
        logging.info(mensaje)
    except Exception as e:
        mensaje = f'Error al modificar: {str:(e)}'
        status = 'Error'
        logging.error(mensaje)

    return {
		  "mensaje":mensaje,
		  "status":status
    }

