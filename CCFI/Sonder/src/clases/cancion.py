class cancion:

    ID = '' 
    nombre = ''
    artista = ''
    letra = ''
    popularidad = ''

    def __init__(self,artista="artista",nombre="nombre",letra="letra") -> None:
        self.ID = "9999"             # autogenerado
        self.artista = artista
        self.nombre = nombre
        self.letra = letra
        self.popularidad = "0"      