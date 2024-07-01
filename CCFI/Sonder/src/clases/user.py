
import csv
import pandas as pd
from clases.cancion import *

# BBDD de canciones
listaCanciones = "BBDD/canciones.csv"


# cualquier usuario podrá buscar una canción
# atributo -> campo por el que buscaremos (artista, cancion o letra)
# valor -> valor dado por el usuario
def buscarCancion(atributo, valor):

    try:

        canciones = []

        # buscamos en la "BBDD"
        with open(listaCanciones, 'r') as archivo:

            archivoCSV = csv.DictReader(archivo)

            for linea in archivoCSV:
                # comparamos el atributo por el que estamos buscando
                if valor in linea[atributo]:
                    # canciones.append(linea["id"])   # retorna los ID de las canciones para su posterior get en la BBDD
                    canciones.append(linea)   # retorna todo

        return canciones
    except: 
        print(f"Error al buscar la canción")
        return False
    
# NUEVO
# lista canciones por popularidad
def listarCanciones():
    try:
        
        df = pd.read_csv(listaCanciones)
        sorted_canciones = df.sort_values(by=["popularidad"], ascending=False)
        # print(sorted_canciones)
        return sorted_canciones
        
    except:
        print(f"Error al listar las canciones")
        return False

# usuario ya logueado
class usuario:

    ID = '' 
    tipo = ''
    nick = ''
    password = ''

    def __init__(self,nick="nick",password="password") -> None:
        self.ID = 12345     # autogenerado
        self.tipo = 1       # 1 -> usuario normal
        self.nick = nick
        self.password = password

    # usuario normal puede añadir canciones
    def anadirCancion(self,cancion):

        try:                                                

            id = cancion.ID                         # del objeto sacamos los atributos
            artista = cancion.artista
            nombre = cancion.nombre
            letra = cancion.letra
            popularidad = cancion.popularidad
            
            fila = [id, artista, nombre, letra, popularidad]    # los junto en un array
            delimitador = ','                                   # defino un delimitador
            linea = delimitador.join(fila)                      # uno los campos del array usando el delimitador
            
            with open(listaCanciones, 'a') as archivo:          # añadimos la linea al fichero
                archivo.write(linea+"\n")
                return True
            
        except:   
            print("Error al añadir la canción")
            return False 
        
    # modificar la letra de una cancion
    def modificarLetra(self, id, letra):

        try:
            df = pd.read_csv(listaCanciones)
            df.loc[df['id'] == id, 'letra'] = letra      
            # print(df)
            df.to_csv(listaCanciones, index=False)      

            return True
        except:
            print(f"Error al modificar letra")
            return False


class admin(usuario):

    def __init__(self, nick="nick", password="password") -> None:
        super().__init__(nick, password)
        self.ID = "9999"
        self.tipo = "2"     # 2 -> admin

    def borrarCancion(self, id):

        lineas = []        

        try:
            
            with open(listaCanciones, "r") as file:         #buscamos las lineas donde aparezca el ID
                for linea in file:
                    if id not in linea:
                        lineas.append(linea)
            
            with open(listaCanciones, "w") as file:         # sobreescribimos el archivo
                file.writelines(lineas)

            return True
        except:
            print("Error al borrar la canción")
            return False


    def anadirLote(self, lote):

        try:
        
            with open (listaCanciones ,"a") as archivo:
                with open (lote, "r") as leer:
                    leer.readline()
                    for linea in leer:
                        archivo.write(linea)

            return True
        except:
            print("Error al cargar el lote")
            return False




